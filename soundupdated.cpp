#include <QCoreApplication>
#include <QAudioInput>
#include <QAudioOutput>
#include <QFile>
#include <QTextStream>
#include <QVBoxLayout>
#include <QLabel>
#include <QWidget>
#include <QMediaPlayer>
#include <QApplication>

class AudioRecorder : public QObject
{
    Q_OBJECT
public:
    AudioRecorder() : audioOutput(nullptr) {}

    void startRecording()
    {
        QAudioFormat format;
        format.setSampleRate(44100);
        format.setChannelCount(1);
        format.setSampleSize(16);
        format.setCodec("audio/pcm");
        format.setByteOrder(QAudioFormat::LittleEndian);
        format.setSampleType(QAudioFormat::SignedInt);

        QAudioDeviceInfo info(QAudioDeviceInfo::defaultInputDevice());
        if (!info.isFormatSupported(format)) {
            qWarning() << "Default format not supported, trying to use the nearest.";
            format = info.nearestFormat(format);
        }

        audioInput.reset(new QAudioInput(format));
        audioInput->start(&buffer);
    }

    void stopRecording()
    {
        audioInput->stop();
        audioInput.reset();
    }

    void playRecording()
    {
        audioOutput.reset(new QAudioOutput(buffer.format()));
        audioOutput->start(&buffer);
    }

};

int main(int argc, char *argv[])
{
    QApplication app(argc, argv);

    // Создаем окно
    QWidget window;
    QVBoxLayout layout(&window);
    QLabel label1("Текст 1");
    QLabel label2("Текст 2");

    layout.addWidget(&label1);
    layout.addWidget(&label2);

    // Создаем объект записи и воспроизведения аудио
    AudioRecorder recorder;

    // Создаем кнопки для управления записью и воспроизведением
    QPushButton recordButton("Запись");
    QPushButton stopButton("Остановить");
    QPushButton playButton("Воспроизведение");
    QPushButton playFileButton("Воспроизведение файла");

    // Подключаем кнопки к соответствующим слотам
    QObject::connect(&recordButton, &QPushButton::clicked, [&recorder]() {
        recorder.startRecording();
    });

    QObject::connect(&stopButton, &QPushButton::clicked, [&recorder]() {
        recorder.stopRecording();
    });

    QObject::connect(&playButton, &QPushButton::clicked, [&recorder]() {
        recorder.playRecording();
    });

    QObject::connect(&playFileButton, &QPushButton::clicked, []() {
        QMediaPlayer mediaPlayer;
        mediaPlayer.setMedia(QUrl::fromLocalFile("/path/to/audio/file")); // Замените "/path/to/audio/file" на путь к вашему аудиофайлу
        mediaPlayer.play();
    });

    // Добавляем кнопки в окно
    layout.addWidget(&recordButton);
    layout.addWidget(&stopButton);
    layout.addWidget(&playButton);
    layout.addWidget(&playFileButton);

    // Отображаем окно
    window.show();

    return app.exec();
}

#include "main.moc"