from vkbottle import Bot, Message
from vkbottle.branch import Branch, ExitBranch
from random import choice
from vkbottle.api.keyboard import keyboard_gen

keyboard_referall_prop = keyboard_gen(
    [
        [{"text": "Пропустить", "color": "negative"}],  # Это первый ряд кнопок
    ],
    inline=False,
)
keyboard_blank = keyboard_gen(
    [
    ],
    inline=False,
)
keyboard_chat = keyboard_gen(
    [
        [{"text": "Стоп", "color": "negative"}],  # Это первый ряд кнопок
        [{"text": "Получить ссылку на пользователя", "color": "positive"}],  # Это второй ряд
    ],
    inline=False,
)
users = {}
users_referal = {}
users_ssilki = {}
bot = Bot("70a1b853168f9ae98005c7b3dac5487a1ceca71f238029e4fdf1d1283527c3e482df098b79f238d873970")


@bot.on.message(text='начать', lower=True)
async def wrapper(ans: Message):
    if ans.from_id not in users:
        users[ans.from_id] = 'USER'
        users_referal[ans.from_id] = 'NEW'
        users_ssilki[ans.from_id] = 5
    await ans('Приветствуем тебя в нашем чате')
    await ans('Отправьте ссылку на пользователя, который пригласил вас, если никто вас не приглашал, то нажмите Пропустить',
              keyboard=keyboard_referall_prop)
    await bot.branch.add(ans.peer_id, "referall")


@bot.branch.simple_branch("referall")
async def branch(ans: Message):
    if ans.text.lower() == 'пропустить':
        await bot.branch.exit(ans.peer_id)
        users_referal[ans.from_id] = 0
        await ans('Напишите Поиск, чтобы найти собеседника', keyboard=keyboard_blank)
    else:
        if users_referal[ans.from_id] == 'NEW':
            polzovatel = ans.text.split('https://vk.com/')
            suren = await bot.api.users.get(user_ids=polzovatel[1])
            suren = suren[0].id
            if ans.from_id == suren:
                await ans('Вы не можете кинуть свою страницу, введите ссылку на другого пользователя')
            elif suren not in users:
                await ans('Этот пользователь не пользуется нашим ботом, введите ссылку на другого пользователя')
            else:
                users_referal[ans.from_id] = suren
                await ans('Вы и этот пользователь получили 5 бесплатных ссылок на пользователей')
                users_ssilki[ans.from_id] = users_ssilki.get(ans.from_id) + 5
                users_ssilki[suren] = users_ssilki.get(suren) + 5
                await bot.branch.exit(ans.peer_id)
                await ans('Напишите Поиск, чтобы найти собеседника', keyboard=keyboard_blank)
        else:
            await ans('Вы уже вводили рефералл', keyboard=keyboard_blank)
            await bot.branch.exit(ans.peer_id)


@bot.on.message(text=['поиск', '!н', 'п', ], lower=True)
async def wrapper(ans: Message):
    await ans('ищем тебе собеседника')
    hosts = []
    for i in users:
        if users[i] == 'HOST':
            hosts.append(i)

    if len(hosts) == 0:
        users[ans.from_id] = 'HOST'
    else:
        uno_host = choice(hosts)
        await ans('мы нашли собеседника', keyboard=keyboard_chat)
        await ans('мы нашли собеседника', user_id=uno_host, keyboard=keyboard_chat)
        users[uno_host] = ans.from_id
        users[ans.from_id] = uno_host
        await bot.branch.add(ans.peer_id, "chat")
        await bot.branch.add(users[ans.peer_id], "chat")


@bot.branch.simple_branch("chat")
async def branch(ans: Message):
    if ans.text.lower() == "стоп":
        await ans('ты вышел из чата', keyboard=keyboard_blank)
        await ans('собеседник вышел из чата', user_id=users[ans.peer_id], keyboard=keyboard_blank)
        await bot.branch.exit(ans.peer_id)
        await bot.branch.exit(users[ans.peer_id])
        users[users[ans.from_id]] = 'USER'
        users[ans.from_id] = 'USER'
    elif ans.text.lower() == 'получить ссылку на пользователя':
        if users_ssilki[ans.from_id] != 0:
            await ans(f'Вот ссылка на пользователя https://vk.com/id{users[ans.from_id]}')
            users_ssilki[ans.from_id] = users_ssilki.get(ans.from_id) - 1
        else:
            await ans('У вас закончили получения ссылок, вы можете купить еще')
    else:
        if ans.attachments != [] and ans.text != '':
            flag = True
            for i in ans.attachments:
                if i.type == 'photo':
                    owner_id = i.photo.owner_id
                    photo_id = i.photo.id
                    access_key = i.photo.access_key
                elif i.type == 'video':
                    owner_id = i.video.owner_id
                    photo_id = i.video.id
                    access_key = i.video.access_key
                else:
                    await ans('Этот тип вложения не поддерживается')
                    break
                if flag:
                    await ans(message=ans.text,
                              attachment=f'{i.type}{owner_id}_{photo_id}_{access_key}', user_id=users[ans.from_id])
                    flag = False
                else:
                    await ans(attachment=f'{i.type}{owner_id}_{photo_id}_{access_key}', user_id=users[ans.from_id])
        elif ans.attachments != [] and ans.text == '':
            for i in ans.attachments:
                if i.type == 'photo':
                    owner_id = i.photo.owner_id
                    photo_id = i.photo.id
                    access_key = i.photo.access_key
                elif i.type == 'video':
                    owner_id = i.video.owner_id
                    photo_id = i.video.id
                    access_key = i.video.access_key
                else:
                    await ans('Этот тип вложения не поддерживается')
                    break
                await ans(attachment=f'{i.type}{owner_id}_{photo_id}_{access_key}', user_id=users[ans.from_id])
        else:
            await ans(message=ans.text, user_id=users[ans.from_id])


@bot.on.message(lower=True)
async def info(ans: Message):
    # await ans(f'У вас осталось {users_ssilki[ans.from_id]} ссылок(ки)')
    if ans.attachments != []:
        owner_id = ans.attachments[0].photo.owner_id
        photo_id = ans.attachments[0].photo.id
        access_key = ans.attachments[0].photo.access_key
        await ans(ans.attachments[0].type)
        exit()
        await ans(attachment=f'{ans.attachments[0].type}{owner_id}_{photo_id}_{access_key}')
bot.run_polling()
