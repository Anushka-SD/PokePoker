from button import Button
from prettytable import PrettyTable
from pygame import mixer
import mysql.connector
import pygame
import pygame_gui
import sys

pygame.init()

'''ONLY RANKS WORKING'''


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
    


def shop():
    while True:
        SHOP_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")
         
        
        #get_user_name()

        SHOP_TEXT = get_font(45).render("This is the SHOP screen.", True, "Black")
        SHOP_RECT = SHOP_TEXT.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        SCREEN.blit(SHOP_TEXT, SHOP_RECT)

        # Adjusted position of the back button to the bottom-right corner
        SHOP_BACK = Button(image=None, pos=(screen_width - 200, screen_height - 100), 
                           text_input="BACK", font=get_font(BACK_BUTTON_TEXTSIZE), base_color="Black", hovering_color="Green")

        SHOP_BACK.changeColor(SHOP_MOUSE_POS)
        SHOP_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if SHOP_BACK.checkForInput(SHOP_MOUSE_POS):
                    main_menu()

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

# def ranks():
#         try:
#             rank_order=get_all_ranks()
#         except mysql.connector.Error as error:
#             print("MySQL Error:", error)
#         # Handle the error as per your application's requirements
#         # For example, display an error message to the user or log the error
#             return

#         # Display the results in the Pygame window
#         while True:
            
#             # print(rank_order)
#             RANKS_MOUSE_POS = pygame.mouse.get_pos()

#             SCREEN.fill("light blue")
             
#             y_offset = 50  # Vertical offset for displaying rows

#             # Render column headers
#             header_font = get_font(OPTIONS_BUTTON_TEXTSIZE // 2)
#             header_text = header_font.render("Username     Points     Rank", True, "Black")
#             header_rect = header_text.get_rect(center=(screen_width // 2, y_offset))
#             SCREEN.blit(header_text, header_rect)
#             y_offset += 50  # Increase y_offset for next row

#             # Render each row of the result set
#             row_font = get_font(25)
#             for row in rank_order:
#                 row_text = row_font.render(f"{row[0]}          {row[1]}          {row[2]}", True, "Black")
#                 row_rect = row_text.get_rect(center=(screen_width // 2, y_offset))
#                 SCREEN.blit(row_text, row_rect)
#                 y_offset += 30  # Increase y_offset for next row

#             # Adjusted position of the back button to the bottom-right corner
#             RANKS_BACK = Button(image=None, pos=(screen_width - 200, screen_height - 100), 
#                                 text_input="BACK", font=get_font(BACK_BUTTON_TEXTSIZE), base_color="Black", hovering_color="Green")

#             RANKS_BACK.changeColor(RANKS_MOUSE_POS)
#             RANKS_BACK.update(SCREEN)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if RANKS_BACK.checkForInput(RANKS_MOUSE_POS):
#                         main_menu()

#             pygame.display.update()



def ranks():
    
    ranks_bg = pygame.transform.scale(pygame.image.load("assets/RanksBackground.png"), (screen_width, screen_height))
    
    try:
        rank_order = get_all_ranks()
    except mysql.connector.Error as error:
        print("My[]\+*98\=-094r2w`1q    SQL Error:", error)
        # Handle the error as per your application's requirements
        # For example, display an error message to the user or log the error
        return

    # Display the results in a table format using PrettyTable
    table = PrettyTable(["Username", "Points", "Rank"])
    for row in rank_order:
        table.add_row(row)

    print(table)  # Print the table to the console

    # Display the table in the Pygame window
    while True:
        RANKS_MOUSE_POS = pygame.mouse.get_pos()

        # SCREEN.fill("light blue")
        SCREEN.blit(ranks_bg, (0, 0))

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

def logs():
    while True:
        MATCHDATA_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("yellow")
         

        MATCHDATA_TEXT = get_font(45).render("This is the MATCHDATA screen.", True, "Black")
        MATCHDATA_RECT = MATCHDATA_TEXT.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        SCREEN.blit(MATCHDATA_TEXT, MATCHDATA_RECT)

        # Adjusted position of the back button to the bottom-right corner
        MATCHDATA_BACK = Button(image=None, pos=(screen_width - 200, screen_height - 100), 
                                text_input="BACK", font=get_font(BACK_BUTTON_TEXTSIZE), base_color="Black", hovering_color="Green")

        MATCHDATA_BACK.changeColor(MATCHDATA_MOUSE_POS)
        MATCHDATA_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if MATCHDATA_BACK.checkForInput(MATCHDATA_MOUSE_POS):
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




'''DRIVER CODE'''
title_screen()  # Display the title screen first
main_menu()