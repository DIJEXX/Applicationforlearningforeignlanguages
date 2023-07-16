#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <Windows.h>
#include <conio.h>

using namespace std;

string sentences[] = {
    "Hello, how are you?",            // Пример предложений на английском
    "What is your name?",
    "Where are you from?",
    "I love programming!",
    "Have a nice day!"
};

string translations[] = {
    "Привет, как дела?",             // Примеры соответствующих переводов на русский
    "Как тебя зовут?",
    "Откуда ты?",
    "Я люблю программирование!",
    "Хорошего дня!"
};

int currentSentenceIndex = 0;
string currentSentence;
string currentTranslation;

void showSentence() {
    system("CLS");
    cout << "Translate the following sentence from English to Russian:\n\n";
    cout << currentSentence << endl;
}

void checkTranslation(string input) {
    if (input == currentTranslation) {
        cout << "Correct translation!" << endl;
    } else {
        cout << "Incorrect translation." << endl;
    }
    _getch();
    showSentence();
}

void getNextSentence() {
    currentSentenceIndex++;
    if (currentSentenceIndex >= sizeof(sentences) / sizeof(sentences[0])) {
        currentSentenceIndex = 0;
    }
    currentSentence = sentences[currentSentenceIndex];
    currentTranslation = translations[currentSentenceIndex];
    showSentence();
}

int main() {
    srand(static_cast<unsigned int>(time(0)));

    // Инициализация окна
    HWND console = GetConsoleWindow();
    RECT r;
    GetWindowRect(console, &r);
    MoveWindow(console, r.left, r.top, 800, 400, TRUE);

    currentSentenceIndex = rand() % (sizeof(sentences) / sizeof(sentences[0]));
    currentSentence = sentences[currentSentenceIndex];
    currentTranslation = translations[currentSentenceIndex];

    showSentence();

    while (true) {
        string input;
        getline(cin, input);

        if (input == "check") {
            cout << "Checking translation..." << endl;
            string translation;
            getline(cin, translation);
            checkTranslation(translation);
        } else if (input == "next") {
            cout << "Next sentence..." << endl;
            getNextSentence();
        }
    }

    return 0;
}