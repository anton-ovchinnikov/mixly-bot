from emoji import emojize

START_MESSAGE = ':wave:'
START_MESSAGE = emojize(START_MESSAGE, language='alias')

PROFILE_MESSAGE = ':bust_in_silhouette: <b>Профиль</b>\n' \
                  f'{":heavy_minus_sign:" * 12}\n' \
                  'ID: <code>{id}</code>\n' \
                  'Username: <code>{username}</code>\n' \
                  'Дата регистрации: <code>{registered_at}</code>'
PROFILE_MESSAGE = emojize(PROFILE_MESSAGE, language='alias')

FIRST_CATALOG_MESSAGE = ':musical_note: <b>Каталог</b>\n' \
                        f'{":heavy_minus_sign:" * 12}'
FIRST_CATALOG_MESSAGE = emojize(FIRST_CATALOG_MESSAGE, language='alias')
SECOND_CATALOG_MESSAGE = f'{":heavy_minus_sign:" * 12}\n\n' \
                         'Воспользуйтесь кнопками навигации ниже.'
SECOND_CATALOG_MESSAGE = emojize(SECOND_CATALOG_MESSAGE, language='alias')
AUDIO_CATALOG_MESSAGE = '<b>{performer} - {title}</b>'

ADD_AUDIO_TITLE_MESSAGE = ':pencil2: <b>Введите название музыки:</b>'
ADD_AUDIO_TITLE_MESSAGE = emojize(ADD_AUDIO_TITLE_MESSAGE, language='alias')
ADD_AUDIO_PERFORMER_MESSAGE = ':pencil2: <b>Введите исполнителя музыки:</b>'
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
MODERATION_CHANGE_TITLE_MESSAGE = ':pencil2: <b>Введите новое название музыки:</b>'
MODERATION_CHANGE_TITLE_MESSAGE = emojize(MODERATION_CHANGE_TITLE_MESSAGE, language='alias')
SUCCESS_CHANGE_TITLE_MESSAGE = ':heavy_check_mark: Название музыки успешно изменено!'
SUCCESS_CHANGE_TITLE_MESSAGE = emojize(SUCCESS_CHANGE_TITLE_MESSAGE, language='alias')
MODERATION_CHANGE_PERFORMER_MESSAGE = ':pencil2: <b>Введите нового исполнителя музыки:</b>'
MODERATION_CHANGE_PERFORMER_MESSAGE = emojize(MODERATION_CHANGE_PERFORMER_MESSAGE, language='alias')
SUCCESS_CHANGE_PERFORMER_MESSAGE = ':heavy_check_mark: Исполнитель успешно изменен!'
SUCCESS_CHANGE_PERFORMER_MESSAGE = emojize(SUCCESS_CHANGE_PERFORMER_MESSAGE, language='alias')
MODERATION_CHANGE_AUDIO_FILE_MESSAGE = ':musical_note: Отправьте аудио файл с музыкой:'
MODERATION_CHANGE_AUDIO_FILE_MESSAGE = emojize(MODERATION_CHANGE_AUDIO_FILE_MESSAGE, language='alias')
SUCCESS_CHANGE_AUDIO_FILE_MESSAGE = ':heavy_check_mark: Аудио файл успешно изменен!'
SUCCESS_CHANGE_AUDIO_FILE_MESSAGE = emojize(SUCCESS_CHANGE_AUDIO_FILE_MESSAGE, language='alias')
MODERATION_DECLINE_MESSAGE = ':pencil2: Введите причину отказа:'
MODERATION_DECLINE_MESSAGE = emojize(MODERATION_DECLINE_MESSAGE, language='alias')
SUCCESS_DECLINE_MESSAGE = ':heavy_check_mark: Вы успешно отклонили музыку!'
SUCCESS_DECLINE_MESSAGE = emojize(SUCCESS_DECLINE_MESSAGE, language='alias')
SUCCESS_ACCEPT_MESSAGE = ':heavy_check_mark: Вы успешно одобрили музыку!'
SUCCESS_ACCEPT_MESSAGE = emojize(SUCCESS_ACCEPT_MESSAGE, language='alias')

DECLINE_USER_MESSAGE = ':x: <b>Администратор отклонил вашу музыку\n<code>{title}</code> по причине:</b>\n' \
                       '{reason}'
DECLINE_USER_MESSAGE = emojize(DECLINE_USER_MESSAGE, language='alias')
ACCEPT_USER_MESSAGE = ':white_check_mark: <b>Администратор одобрил вашу музыку <code>{title}</code></b>\n' \
                      'Теперь вы можете найти ее в каталоге.'
ACCEPT_USER_MESSAGE = emojize(ACCEPT_USER_MESSAGE, language='alias')

CANCEL_MESSAGE = ':x: Действие отменено!'
CANCEL_MESSAGE = emojize(CANCEL_MESSAGE, language='alias')

INDEV_MESSAGE = ':hammer: <b>В разработке!</b>'
INDEV_MESSAGE = emojize(INDEV_MESSAGE, language='alias')
