from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.tab import MDTabsBase
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivy.uix.screenmanager import (ScreenManager, Screen)

item = """

TwoLineIconListItem:
	text: "Sj Bros"
	secondary_text: "Contact"
	on_press: app.open_contact(*args)
				
	ImageLeftWidget:
		source: "result.png"

"""

class Tab(FloatLayout, MDTabsBase):
	'''Class implementing content for a tab.'''


class MainScreen(Screen):
	pass

class SettingsScreen(Screen):
	pass


class NewGroupScreen(Screen):
	pass


class NewBrodcastScreen(Screen):
	pass


class WhatsAppWebScreen(Screen):
	pass


class StarredMessagesScreen(Screen):
	pass


class PaymentsScreen(Screen):
	pass




		

class MainApp(MDApp):
	def build(self):
		self.theme_cls.primary_palette = "Green"
		self.title = "Whatsapp"
		self.root = Builder.load_file("design.kv")
		
		
	
	def inspect(self, text):
		self.title = text
		
		

	def on_start(self):
		lst = self.root.get_screen("main").ids.list
		for i in range(1,31):
			list_item = item
			lst.add_widget(Builder.load_string(list_item))



	def menu(self, instance):
		print("Function 'menu' accessed")
		self.root.ids.settings.manager.current = instance.text.lower().replace(' ', '')
		print("Changed to screen:",instance.text)	
	
	
	
	def show_more(self):
		menu_items = [
		{'text': 'New Group'}, 
		{'text': 'New Brodcast'}, 
		{'text': 'WhatsApp Web'}, 
		{'text': 'Starred Messages'}, 
		{'text': 'Payments'}, 
		{'text': 'Settings'}
						]
		self.main_screen_more_menu = self.create_menu(self.root.get_screen("main").ids.more_menu_caller, menu_items)
		self.main_screen_more_menu.open()
		
		
		
	def open_contact(self, obj):
		print(obj.text)
	
	
	
	# Function to create DropDownMenu
	def create_menu(self, callfrom, menu_items):
		menu = MDDropdownMenu(caller = callfrom, items = menu_items, width_mult = 4, callback = self.menu)
		return menu
		
	
	
	def on_stop(self):
		raise ValueError("Your Program has worked Successfully!")



if __name__ == "__main__":
	MainApp().run()