
from button import Button
import pygame
import pygame_gui
import mysql.connector
import main_3
from slider import Slider
import sys


pygame.init()
     
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



manager = pygame_gui.UIManager((screen_width, screen_height))

text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                               object_id='#main_text_entry')

clock = pygame.time.Clock()

def buy_pokemon(pokemon_name):
    return

def show_user_name_to_buy(user_name,pokemon_name):
    # Query the database to check if the user exists
    user_exists = check_user_exists(user_name)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        SCREEN.fill("white")
        
        if user_exists:
            # If the user exists, display a welcome message
            new_text = get_font(BACK_BUTTON_TEXTSIZE).render(f"Welcome back, {user_name}!", True, "black")
            USER_MOUSE_POS = pygame.mouse.get_pos()
            create_generic_back_button(USER_MOUSE_POS,"BUY",buy_pokemon(pokemon_name))
            
        else:
            # If the user is new, display a registration message
            new_text = get_font(BACK_BUTTON_TEXTSIZE).render(f"Hello, {user_name}!\nYou Are A New User!!\nJoin Our Team By Playing Some Battles <3",
                                                             True, "black")
            USER_MOUSE_POS = pygame.mouse.get_pos()
            create_generic_back_button(USER_MOUSE_POS,"BACK",main_menu())
        
        new_text_rect = new_text.get_rect(center=(screen_width // 2, screen_height // 2))
        SCREEN.blit(new_text, new_text_rect)

        clock.tick(60)

        manager.draw_ui(SCREEN)
        
        pygame.display.update()

def get_user_name_to_buy(pokemon_name):
    while True:
        UI_REFRESH_RATE = clock.tick(60)/1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if (event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and
                event.ui_object_id == '#main_text_entry'):
                show_user_name_to_buy(event.text,pokemon_name)
            
            manager.process_events(event)
        
        manager.update(UI_REFRESH_RATE)
        
        SCREEN.fill("white")

        manager.draw_ui(SCREEN)
        
        pygame.display.update()

def check_user_exists(user_name):
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Query to check if the user exists
        query = "SELECT COUNT(*) FROM users WHERE username = %s"
        cursor.execute(query, (user_name,))
        count = cursor.fetchone()[0]

        cursor.close()
        connection.close()
        
        return count > 0  # Return True if count is greater than 0 (user exists), False otherwise

    except mysql.connector.Error as error:
        print("MySQL Error:", error)
        return False  # Return False in case of any error or exception
 
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
    card_margin = 30
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
        button_font = get_font(19)
        for pokemon in available_pokemon:
            card_y = current_row * (card_height + card_margin) - slider.scroll_position
            pokemon_name = pokemon[1]
            card_image = card_images[pokemon_name]

            card_rect = pygame.Rect(card_margin + current_column * (card_width + card_margin), card_y,
                                     card_width, card_height)

            # Create a Button instance for the text below the card
            button_text = pokemon_name
            button_pos = (card_rect.centerx, card_rect.bottom + 10)
            card_button = Button(image=None, pos=button_pos, text_input=button_text, font=button_font,
                                 base_color="Black", hovering_color="Green")

            # Check for mouse interaction with the button
            card_button.changeColor(SHOP_MOUSE_POS)
            card_button.update(SCREEN)
            if card_button.checkForInput(SHOP_MOUSE_POS) and pygame.mouse.get_pressed()[0]:
                # Perform action when the button is clicked (e.g., select the card)
                # print(f"Clicked on {pokemon_name}")
                get_user_name_to_buy(pokemon_name)

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
        button_font = main_3.get_font(button_font_size)
        BACK_BUTTON = Button(image=None, pos=(screen_width - button_width + 20, screen_height - button_height - button_margin),
                             text_input="BACK", font=button_font, base_color="Black", hovering_color="Green")
        BACK_BUTTON.changeColor(SHOP_MOUSE_POS)
        BACK_BUTTON.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(SHOP_MOUSE_POS):
                    main_3.main_menu()  # Go back to the main menu

        pygame.display.update()
