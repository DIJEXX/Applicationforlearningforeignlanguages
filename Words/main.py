from kivy.config import Config
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.modalview import ModalView
from kivy.properties import ObjectProperty
from kivy.factory import Factory
from check import Check
import pandas as pd
import random
from kivy.core.window import Window

Window.clearcolor = (0, 0, 0, 1)
Config.set('graphics', 'fullscreen', 0)
Config.set('graphics', 'height', 1080)
Config.set('graphics', 'width', 1920)
Config.write()

class Popup_m():
    def popup_menu(
                    self,
                    cont_key='menu',
                    sizes=(0.5, 0.5),
                    position={'right': 1, 'top': 1},
                    **kwargs
                    ):
        popup_window = ModalView(
            size_hint=sizes,
            pos_hint=position)
        if cont_key == 'menu':
            content = Menu()
        elif cont_key == 'open_file':
            content = Open_file()
            content.turn_on(pw = popup_window)
        elif cont_key == 'save_file':
            content = Save_file()
            content.turn_on(pw = popup_window)
        elif cont_key == 'clear_dict':
            content = Confirm_popup()
            content.turn_on(text_to_label='Statistics of the dictionary will be cleared.\nAre you sure?',
                            text_to_button='Yes', func_key='clear_dict', pw = popup_window)
        elif cont_key == 'statistics':
            content = Confirm_popup()
            content.turn_on(text_to_label='', text_to_button='Ок', func_key='stats + popup_dismiss', pw = popup_window)
        elif cont_key == 'learned_popup':
            content = Confirm_popup()
            content.turn_on(pw = popup_window)
        elif cont_key == 'dict_not_imported_popup':
            content = Confirm_popup()
            content.turn_on(text_to_label='Import dictionary, please', text_to_button='Import', func_key='import_dict', pw = popup_window)
        else:
            content = Confirm_popup()
            content.turn_on(text_to_label = cont_key, text_to_button='Ок', func_key = 'popup_dismiss', pw = popup_window)
        popup_window.add_widget(content)
        popup_window.open()
class Func(Check):
    def __init__(self, *args, **kwargs):
        self.current_card = 0
        self.app = App.get_running_app()
        self.ch = Check()
        self.txt_size = 1
    def import_dictionary(self,file_pass):
        try:
            dict = pd.read_csv(file_pass[0], delimiter='|')
            answer, message = self.ch.check_dict(dict)
        except:
            answer, message = None, 'Wrong file extention or data.\nCSV file required'
        if answer is not None:
            self.data = answer
            self.current_card = pd.DataFrame({'Showed' : [0]}).iloc[0]
            self.progress_update()
            self.show_card(mode='random')
        else:
            self.popup_menu (cont_key = message, sizes = (0.65, 0.3), position = {'center_x': 0.5, 'center_y': 0.5})
            return ()
    def progress_update(self):
        self.progress_bar.max = len(self.data.index)
        self.progress_bar.value = len(self.data[self.data.Learned == True].index)
    def show_card(self, mode='random', learned=False):
        ccn = self.current_card.name  # индекс current_card в data
        self.data.loc[ccn, 'Showed'] += 1
        if learned == True:
            self.data.loc[ccn, 'Learned'] = True
            self.progress_update()
        self.app.root.label_2.text = ''
        self.current_card = self.data[self.data.Learned == False].sample().iloc[0]
        if mode == 'forward':
            cc_word = self.current_card.Word
            self.cc_translation = self.current_card.Translation
        if mode == 'reverse':
            cc_word = self.current_card.Translation
            self.cc_translation = self.current_card.Word
        if mode == 'random':
            cc_word = random.choice([self.current_card.Word, self.current_card.Translation])
            if cc_word == self.current_card.Word:
                self.cc_translation = self.current_card.Translation
            else:
                self.cc_translation = self.current_card.Word
        self.app.root.label_1.text = cc_word
    def check_translation(self):
        self.app.root.label_2.text = self.cc_translation
        print(self.button_learned.height, self.button_learned.size)
    def dict_presence(self, cont_key, direction = 0):
        if direction == 0:
            if type(self.current_card) is int:
                self.popup_menu(cont_key = 'dict_not_imported_popup', sizes = (0.65, 0.3), position = {'center_x': 0.5, 'center_y': 0.5})
            else:
                if cont_key == 'clear_dict':
                    self.popup_menu(cont_key='clear_dict', sizes=(0.65, 0.3), position={'center_x': 0.5, 'center_y': 0.5})
                elif cont_key == 'statistics':
                    self.popup_menu(cont_key='statistics')
                elif cont_key == 'save_file':
                    self.popup_menu(cont_key='save_file', sizes = (0.7, 0.7))
                # кнопки основного окна:
                elif cont_key == 'learned_popup':
                    self.popup_menu(cont_key='learned_popup', sizes=(0.65, 0.3), position={'center_x': 0.5, 'center_y': 0.5})
                elif cont_key == 'show_card':
                    self.show_card()
                elif cont_key == 'check_translation':
                    self.check_translation()
        elif direction == 1:
            self.popup_menu(cont_key='open_file', sizes=(0.7, 0.7))
            if type(self.current_card) is not int:
                self.popup_menu(cont_key='If import new dictionary before saving current one, current statistics will be lost', sizes=(0.65, 0.3),
                                position={'center_x': 0.5, 'center_y': 0.5})
    def clear_dictionary(self):
        self.data['Showed'] = 0
        self.data['Learned'] = 0
        self.progress_update()
class Menu(AnchorLayout, Popup_m):
    anchor_x = 'left'
    anchor_y = 'top'
class Open_file(AnchorLayout):
    anchor_x ='left'
    anchor_y='top'
    o_f_filechooser = ObjectProperty()
    o_f_button = ObjectProperty()
    def turn_on(self, pw):
        self.app = App.get_running_app()
        self.pw = pw
        self.o_f_button.bind(on_release = self.of_but_import_dict)
    def of_but_import_dict(self, instance):
        self.pw.dismiss()
        self.app.root.import_dictionary(self.o_f_filechooser.selection)
class Save_file(AnchorLayout):
    anchor_x = 'left'
    anchor_y = 'top'
    s_f_filechooser = ObjectProperty()
    s_f_text_input = ObjectProperty()
    s_f_cancel_button = ObjectProperty()
    s_f_save_button = ObjectProperty()
    def turn_on(self, pw):
        self.app = App.get_running_app()
        self.pw = pw
        self.s_f_cancel_button.bind(on_release=self.pw.dismiss)
        self.s_f_save_button.bind(on_release=self.sf_but_export_dict)
    def sf_but_export_dict(self, instance):
        self.pw.dismiss()
        try:
            if self.s_f_text_input.text.find(self.s_f_filechooser.path) == 0:
                adress = self.s_f_text_input.text
            elif self.s_f_text_input.text.find(self.s_f_filechooser.path) == -1:
                if self.s_f_filechooser.path[-1] != '\\':
                    adress = self.s_f_filechooser.path + '\\' + self.s_f_text_input.text
                else:
                    adress = self.s_f_filechooser.path + self.s_f_text_input.text
            else:
                self.app.root.popup_menu(cont_key = 'Probably, wrong adress, filename or extention', sizes = (0.65, 0.3), position = {'center_x': 0.5, 'center_y': 0.5})
                return()
            self.app.root.data.to_csv(adress, sep = '|')
        except:
            self.app.root.popup_menu(cont_key='No access to disk or another mistake',
                                     sizes=(0.65, 0.3), position={'center_x': 0.5, 'center_y': 0.5})
class Confirm_popup(AnchorLayout):
    label_popup = ObjectProperty()
    button_popup = ObjectProperty()
    def turn_on(self, pw, text_to_label='Sure?', text_to_button='Yes', func_key='show_card'):
        self.app = App.get_running_app()
        self.pw = pw
        self.label_popup.text = text_to_label
        self.button_popup.text = text_to_button
        if func_key == 'import_dict':
            self.button_popup.bind(on_release = self.cp_but_import_dict)
        elif func_key == 'show_card':
            self.button_popup.bind(on_release = self.cp_but_show_card)
        elif func_key == 'clear_dict':
            self.button_popup.bind(on_release = self.cp_but_clear_dict)
        elif func_key == 'popup_dismiss':
            self.button_popup.bind(on_release = self.pw.dismiss)
        elif func_key == 'stats + popup_dismiss':
            all_cards = len(self.app.root.data.index)
            learned_cards = len(self.app.root.data[self.app.root.data.Learned == True].index)
            learned_cards_p = round(learned_cards / all_cards * 100)
            in_study_cards = all_cards - learned_cards
            in_study_cards_p = round(in_study_cards / all_cards * 100)
            if learned_cards > 0:
                average = round(sum(self.app.root.data[self.app.root.data.Learned == True].Showed) / learned_cards)
            else:
                average = 0
            self.label_popup.text = 'Total in dictionary: {}\nLearned: {} ({}%)\nIn study: {} ({}%)\nOn average showed \nbefore learned: {}'.format(
                all_cards, learned_cards, learned_cards_p, in_study_cards, in_study_cards_p, average)
            self.button_popup.bind(on_release = self.pw.dismiss)
    def cp_but_import_dict(self, instance):
        self.pw.dismiss()
        self.app.root.popup_menu(cont_key='open_file', sizes=(0.7, 0.7))
    def cp_but_show_card(self, instance):
        self.pw.dismiss()
        self.app.root.show_card(learned=True)
    def cp_but_clear_dict(self, instance):
        self.pw.dismiss()
        self.app.root.clear_dictionary()
class Container(BoxLayout, Popup_m, Func):
    progress_bar = ObjectProperty()
    label_1 = ObjectProperty()
    label_2 = ObjectProperty()
    button_menu = ObjectProperty()
    button_learned = ObjectProperty()
    button_next = ObjectProperty()
    button_check = ObjectProperty()
class MyApp(App):
    title = 'Words'
    def build(self):
        self.root = Container()
        return self.root
Factory.register('Container', cls=Container)
Factory.register('Menu', cls=Menu)
Factory.register('Open_file', cls=Open_file)
Factory.register('Confirm_popup', cls=Confirm_popup)
if __name__ == "__main__":
    MyApp().run() 