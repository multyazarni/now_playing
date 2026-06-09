# AIMP Now Playing Window

Небольшое приложение для Windows, которое отображает текущий трек из AIMP в большом полноэкранном окне.
A small Windows app that shows the current track from AIMP in a large fullscreen-style window.

## What it does

- Показывает название текущего трека и исполнителя.
- Показывает предыдущий трек под ним.
- Автоматически сохраняет путь к файлу выбранного трека.
- Может автоматически определять файл "NowPlaying.txt` в общих папках.
- Работает как отдельный файл `.exe`.

- Shows the current track title and artist.
- Shows the previous track below it.
- Saves the selected track file path automatically.
- Can auto-detect the `NowPlaying.txt` file in common folders.
- Works as a standalone `.exe`.

## Requirements

- Windows.
- Установлен AIMP.
- Плагин AIMP, который записывает текущую информацию о треке в текстовый файл.
- Файл трека должен содержать названия треков в виде обычного текста.

- Windows.
- AIMP installed.
- An AIMP plugin that writes current track info to a text file.
- The track file must contain track names in plain text.

## How to use

1. Установите AIMP.
2. Установите и настройте плагин AIMP, который записывает текущий трек в текстовый файл.
3. Убедитесь, что плагин создает файл типа `NowPlaying.txt`.
4. Загрузите последнюю версию этого приложения.
5. Запустите `now_playing.exe`.
6. Нажмите **Выбрать файл**, если приложение не нашло файл автоматически.
7. После выбора файла путь к нему сохраняется автоматически.

1. Install AIMP.
2. Install and configure the AIMP plugin that writes the current track to a text file.
3. Make sure the plugin creates a file like `NowPlaying.txt`.
4. Download the latest release of this app.
5. Run `now_playing.exe`.
6. Click **Select file** if the app did not find the file automatically.
7. After selecting the file, the path is saved automatically.

## File format

Приложение считывает первую строку как текущую дорожку, а вторую строку - как предыдущую дорожку.

The app reads the first line as the current track and the second line as the previous track.

Example:

```text
Preservation Hall Jazz Band - His Eye Is On The Sparrow
Del McCoury - Careless Love
Preservation Hall Jazz Band - Summertime
```

## Configuration

Выбранный путь к файлу сохраняется в файле config.json в той же папке, что и приложение.

Если вы хотите изменить путь, удалите файл config.json и запустите приложение снова.

The selected file path is saved in `config.json` in the same folder as the app.

If you want to reset the path, delete `config.json` and run the app again.

## Download

Готовая к использованию версия для Windows доступна на странице релизов на GitHub.

The ready-to-use Windows version is available in the GitHub Releases page.

## Development

If you want to run the source code:

```powershell
pip install pyinstaller
python now_playing.py
```

To build the executable:

```powershell
pyinstaller --onefile --windowed now_playing.py
```

## Notes

- Если путь к файлу не найден автоматически, используйте ** Выберите файл**.
- Приложение сохраняет выбранный путь к файлу между запусками.
- Окно остается поверх других окон.

- If the file path is not found automatically, use **Select file**.
- The app keeps the selected file path between launches.
- The window stays on top of other windows.