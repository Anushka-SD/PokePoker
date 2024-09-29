from button import Button
from prettytable import PrettyTable
from pygame import mixer
import mysql.connector
import pygame
import pygame_gui
from slider import Slider
import sys

pygame.init()

"""RANKS
SHOP DISPLAY
LOGS WORKING"""
     
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
SCREEN = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menu")

POKE_BUTTON_TEXTSIZE = (int)(screen_height * 0.11)
OPTIONS_BUTTON_TEXTSIZE = (int)(screen_height * 0.08)
BACK_BUTTON_TEXTSIZE = (int)(screen_height * 0.04)

db_config = {
    'user': 'root',
    'password':'root',
    'host':'localhost',
    'database': 'mini_project'
}


BG = pygame.transform.scale(pygame.image.load("assets/Background.png"), (screen_width, screen_height))

def title_screen():
    title_bg = pygame.transform.scale(pygame.image.load("assets/TitleBackground1.png"), (screen_width, screen_height))
    SCREEN.blit(title_bg, (0, 0))
    #playsound('assets/bgm.mp3',True)
    

    while True:
        TITLE_MOUSE_POS = pygame.mouse.get_pos()

        POKE_BUTTON = Button(image=None, pos=(screen_width // 2, screen_height // 9), 
                           text_input="PokePoker", font=get_font(POKE_BUTTON_TEXTSIZE), base_color="black", hovering_color="red")

        POKE_BUTTON.changeColor(TITLE_MOUSE_POS)
        POKE_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if POKE_BUTTON.checkForInput(TITLE_MOUSE_POS):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    main_menu()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.update()

def playsound(soundeffect, is_Looping):
        mixer.init()
        mixer.music.load(soundeffect)
        if is_Looping:
            mixer.music.play(-1)
        else:
            mixer.music.play()
    
def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")
         

        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        # Adjusted position of the back button to the bottom-right corner
        PLAY_BACK = Button(image=None, pos=(screen_width - 200, screen_height - 100), 
                           text_input="BACK", font=get_font(BACK_BUTTON_TEXTSIZE), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()

        pygame.display.update()

# Function to fetch Pokemon info from the database
def fetch_pokemon_info(pokemon_name):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()
        
        # Query to fetch Pokemon info based on name (case insensitive)
        query = "SELECT * FROM new_pokemon WHERE LOWER(name) = LOWER(%s)"
        cursor.execute(query, (pokemon_name,))
        pokemon_info = cursor.fetchone()
        
        connection.close()
        return pokemon_info
    except mysql.connector.Error as error:
        print("MySQL Error:", error)

manager = pygame_gui.UIManager((1600, 900))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                               object_id='#main_text_entry')

clock = pygame.time.Clock()

def show_user_name(user_name):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill("white")

        new_text = get_font(BACK_BUTTON_TEXTSIZE).render(f"Hello, {user_name}", True, "black")
        new_text_rect = new_text.get_rect(center=(screen_width // 2, screen_height // 2))
        SCREEN.blit(new_text, new_text_rect)

        clock.tick(60)

        pygame.display.update()

def get_user_name():
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                show_user_name(event.text)
            
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)

        SCREEN.fill("white")

        manager.draw_ui(SCREEN)

        pygame.display.update()
    
def fetch_available_pokemon_info():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Call the GetAllRanks stored procedure
        cursor.callproc('availablepoke')

        # Fetch all results
        for result in cursor.stored_results():
            rows = result.fetchall()
 
        cursor.close()
        connection.close()
        return rows

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
        return None
 
def load_card_images(available_pokemon, card_width, card_height):
    card_images = {}
    for pokemon in available_pokemon:
        pokemon_name = pokemon[1]
        card_image_path = f"cards/{pokemon_name.lower()}.png"
        card_images[pokemon_name] = pygame.transform.scale(pygame.image.load(card_image_path), (card_width, card_height))
    return card_images   

def shop():
    try:
        available_pokemon = fetch_available_pokemon_info()
    except mysql.connector.Error as error:
        print("MySQL Error:", error)
        return

    card_width = 250
    card_height = 300
    card_margin = 20
    cards_per_row = 5

    total_cards = len(available_pokemon)
    rows = (total_cards + cards_per_row - 1) // cards_per_row
    total_height = rows * (card_height + card_margin) + card_margin

    slider = Slider(screen_width, screen_height, total_height)
    card_images = load_card_images(available_pokemon, card_width, card_height)

    while True:
        SHOP_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("white")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEMOTION:
                slider.handle_event(event)  # Pass mouse events to the slider
            elif event.type == pygame.MOUSEWHEEL:
                # Handle mouse wheel scrolling
                if event.y > 0:  # Scroll up
                    slider.slider_handle_pos -= 10  # Adjust the step size as needed
                    slider.slider_handle_pos = max(0, slider.slider_handle_pos)  # Ensure handle doesn't go above track
                elif event.y < 0:  # Scroll down
                    slider.slider_handle_pos += 10  # Adjust the step size as needed
                    slider.slider_handle_pos = min(slider.slider_height - slider.slider_handle_height, slider.slider_handle_pos)  # Ensure handle doesn't go below track


        slider.update_slider()

        current_row = 0
        current_column = 0
        for pokemon in available_pokemon:
            card_y = current_row * (card_height + card_margin) - slider.scroll_position
            card_rect = pygame.Rect(card_margin + current_column * (card_width + card_margin), card_y,
                                     card_width, card_height)

            pokemon_name = pokemon[1]
            card_image = card_images[pokemon_name]
            SCREEN.blit(card_image, card_rect)

            current_column += 1
            if current_column >= cards_per_row:
                current_column = 0
                current_row += 1

        slider.draw_slider(SCREEN)
        button_width = 100
        button_height = 50
        button_margin = 10
        button_font_size = 20
        button_font = get_font(button_font_size)
        BACK_BUTTON = Button(image=None, pos=(screen_width - button_width - button_margin, screen_height - button_height - button_margin),
                             text_input="BACK", font=button_font, base_color="Black", hovering_color="Green")
        BACK_BUTTON.changeColor(SHOP_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    main_menu()  # Go back to the main menu

        pygame.display.update()

def get_all_ranks():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Call the GetAllRanks stored procedure
        cursor.callproc('GetAllRanks')

        # Fetch all results
        for result in cursor.stored_results():
            rows = result.fetchall()
 
        cursor.close()
        connection.close()
        return rows

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
        return None

def ranks():
    try:
        rank_order = get_all_ranks()
    except mysql.connector.Error as error:
        print("MySQL Error:", error)
        # Handle the error as per your application's requirements
        # For example, display an error message to the user or log the error
        return

    # Display the results in a table format using PrettyTable
    table = PrettyTable(["Username", "Points", "Rank"])
    for row in rank_order:
        table.add_row(row)

    # Display the table in the Pygame window
    while True:
        RANKS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("light blue")

        # Render the table headers
        header_font = get_font(OPTIONS_BUTTON_TEXTSIZE)
        header_text = header_font.render("RANKS", True, "Black")
        header_rect = header_text.get_rect(center=(screen_width // 2, 50))
        SCREEN.blit(header_text, header_rect)

        # Render each row of the table
        row_font = get_font(25)
        y_offset = screen_height // 6
        for line in str(table).splitlines():
            row_text = row_font.render(line, True, "Black")
            row_rect = row_text.get_rect(center=(screen_width // 2, y_offset))
            SCREEN.blit(row_text, row_rect)
            y_offset += 30  # Increase y_offset for next row

        # Adjusted position of the back button to the bottom-right corner
        RANKS_BACK = Button(image=None, pos=(screen_width - 200, screen_height - 100),
                            text_input="BACK", font=get_font(BACK_BUTTON_TEXTSIZE), base_color="Black",
                            hovering_color="Green")

        RANKS_BACK.changeColor(RANKS_MOUSE_POS)
        RANKS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if RANKS_BACK.checkForInput(RANKS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def get_battle_data():
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        query = "SELECT * FROM battle"
        cursor.execute(query)

    # Fetch all rows
        rows = cursor.fetchall()

        cursor.close()
        connection.close()
        return rows

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
        return None

def logs():
    try:
        battle_logs = get_battle_data()
    except mysql.connector.Error as error:
        print("MySQL Error (inlogs):", error)
        # Handle the error as per your application's requirements
        # For example, display an error message to the user or log the error
        return

    # Display the results in a table format using PrettyTable
    table = PrettyTable(["MatchId", "User1P", "User2P","UID1","UID2","Winner"])
    for row in battle_logs:
        table.add_row(row)

    # Display the table in the Pygame window
    while True:
        LOGS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("pink")

        # Render the table headers
        header_font = get_font(OPTIONS_BUTTON_TEXTSIZE)
        header_text = header_font.render("LOGS", True, "Black")
        header_rect = header_text.get_rect(center=(screen_width // 2, 50))
        SCREEN.blit(header_text, header_rect)

        # Render each row of the table
        row_font = get_font(25)
        y_offset = screen_height // 6
        for line in str(table).splitlines():
            row_text = row_font.render(line, True, "Black")
            row_rect = row_text.get_rect(center=(screen_width // 2, y_offset))
            SCREEN.blit(row_text, row_rect)
            y_offset += 30  # Increase y_offset for next row

        # Adjusted position of the back button to the bottom-right corner
        LOGS_BACK = Button(image=None, pos=(screen_width - 200, screen_height - 100),
                            text_input="BACK", font=get_font(BACK_BUTTON_TEXTSIZE), base_color="Black",
                            hovering_color="Green")

        LOGS_BACK.changeColor(LOGS_MOUSE_POS)
        LOGS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if LOGS_BACK.checkForInput(LOGS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

def exit_game():
    pygame.quit()
    sys.exit()

def main_menu():
    while True:
        
        MAINMENU_TITLE_SIZE = (int)(screen_height * 0.12)
        SCREEN.blit(BG, (0, 0))
         

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(MAINMENU_TITLE_SIZE).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(screen_width // 2, screen_height // 9))

        BUTTON_Y_OFFSET = screen_height // 7  # Adjust this value to increase or decrease the gap between buttons
        buttons = [
            {"text": "Start", "function": play},
            {"text": "Shop", "function": shop},
            {"text": "Ranks", "function": ranks},  # Changed to call the rank handling function
            {"text": "Logs", "function": logs},
            {"text": "Exit", "function": sys.exit}
        ]

        for i, button_info in enumerate(buttons):
            button_y = screen_height // 3.5 + i * BUTTON_Y_OFFSET
            
            BUTTON_BG = "assets/General Rect.png"
            
            button = Button(image=pygame.image.load(BUTTON_BG), pos=(screen_width // 2, button_y),
                            text_input=button_info["text"], font=get_font(OPTIONS_BUTTON_TEXTSIZE),
                            base_color="#d7fcd4", hovering_color="White")
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
            if button.checkForInput(MENU_MOUSE_POS):
                if pygame.mouse.get_pressed()[0]:  # Check if left mouse button is pressed
                    button_info["function"]()  # Call the associated function when the button is clicked

        SCREEN.blit(MENU_TEXT, MENU_RECT)
         

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()





title_screen()
main_menu() 