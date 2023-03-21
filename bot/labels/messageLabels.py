from emoji import emojize

START_MESSAGE = ':wave:'
START_MESSAGE = emojize(START_MESSAGE, language='alias')

PROFILE_MESSAGE = ':bust_in_silhouette: <b>Профиль</b>\n' \
                  f'{":heavy_minus_sign:" * 12}\n' \
                  'ID: <code>{id}</code>\n' \
                  'Username: <code>{username}</code>\n' \
                  'Дата регистрации: <code>{registered_at}</code>'
PROFILE_MESSAGE = emojize(PROFILE_MESSAGE, language='alias')

ADD_AUDIO_TITLE_MESSAGE = ':pencil2: <b>Введите название музыки:</b>'
ADD_AUDIO_TITLE_MESSAGE = emojize(ADD_AUDIO_TITLE_MESSAGE, language='alias')
ADD_AUDIO_PERFORMER_MESSAGE = ':pencil2: <b>Введите автора музыки:</b>'
ADD_AUDIO_PERFORMER_MESSAGE = emojize(ADD_AUDIO_PERFORMER_MESSAGE, language='alias')
SUCCESSFUL_ADD_AUDIO_MESSAGE = ':heavy_check_mark: <b>Вы успешно предложили музыку!</b>\n\n' \
                               'Она появится в каталоге после модерации.'
SUCCESSFUL_ADD_AUDIO_MESSAGE = emojize(SUCCESSFUL_ADD_AUDIO_MESSAGE, language='alias')
AUDIO_ALREADY_EXIST_MESSAGE = ':link: <b>Такая музыка уже есть в базе!</b>\n\n' \
                              'Возможно она проходит модерацию, и скоро появится в каталоге.'
AUDIO_ALREADY_EXIST_MESSAGE = emojize(AUDIO_ALREADY_EXIST_MESSAGE, language='alias')

AUDIO_MODERATION_MESSAGE = ':eye: <b>Модерация</b>\n' \
                           f'{":heavy_minus_sign:" * 12}\n' \
                           'Название: <code>{title}</code>\n' \
                           'Исполнитель: <code>{performer}</code>\n' \
                           'Жанр: <code>{genre}</code>'
AUDIO_MODERATION_MESSAGE = emojize(AUDIO_MODERATION_MESSAGE, language='alias')

ADMIN_MENU_MESSAGE = ':key: <b>Админ-панель</b>'
ADMIN_MENU_MESSAGE = emojize(ADMIN_MENU_MESSAGE, language='alias')

NO_AUDIO_FOR_MODERATION_NOTIFY = ':grey_exclamation: Нет музыки для модерации!'
NO_AUDIO_FOR_MODERATION_NOTIFY = emojize(NO_AUDIO_FOR_MODERATION_NOTIFY, language='alias')

CANCEL_MESSAGE = ':x: <b>Действие отменено!</b>'
CANCEL_MESSAGE = emojize(CANCEL_MESSAGE, language='alias')

INDEV_MESSAGE = ':hammer: <b>В разработке!</b>'
INDEV_MESSAGE = emojize(INDEV_MESSAGE, language='alias')
