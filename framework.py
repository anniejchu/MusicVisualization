import pygame
import random
import songanalysis as sa

'''
DEFINING COLORS
'''
black = (0,0,0)
white = (255, 255, 255)
brightred = (255, 69, 0)
brightgreen = (0, 255, 0)
brightblue = (0,0,255)
darkred = (178, 34, 34)
darkgreen = (25, 100, 50)
darkblue = (25, 50, 150)
grey = (30, 30, 30)
teal = (0, 128, 128)
cyan = (0,255, 255)
yellow = (255, 255, 0)
violet = (138, 43, 226)
steelblue = (175, 196, 222)
magenta = (255, 0, 255)
lavender = (230, 230, 250)

color_list = [brightred, brightblue, brightgreen, darkred, darkblue, darkgreen, teal, cyan, yellow, violet, steelblue, magenta, lavender]

#defining screen dimensions
screen_width = 850
screen_height = 900
record_size = 40


#pulling from songanalysis.py file and isolating elements of the list into relevant variables
i_song_info = sa.final_process_i(sa.input)
i_general = i_song_info[0]
i_features = i_song_info[1]
o_song_info = sa.final_process_o(sa.the_second_yeet)
o_general = o_song_info[0]
o_features = o_song_info[1]

#creating color coding baseline
color1 = ['minor', 'not danceable', 'low energy', 'very negative vibes']
color2 = ['kinda danceable', 'negative vibes']
color3 = ['pretty danceable', 'mid energy', 'neutral vibes']
color4 = ['very danceable', 'positive vibes']
color5 = ['major', 'extremely danceable', 'high energy', 'very positive vibes']

#matches each of the color codes to a specific color
def color_code(feature_list):
    x = ''
    color_list = []
    for item in feature_list:
        if item in color1:
            x = darkred
            color_list.append(x)
        if item in color2:
            x = magenta
            color_list.append(x)
        if item in color3:
            x = yellow
            color_list.append(x)
        if item in color4:
            x = brightblue
            color_list.append(x)
        if item in color5:
            x = cyan
            color_list.append(x)
        elif item not in color1 and item not in color2 and item not in color3 and item not in color4 and item not in color5:
            x = lavender
            color_list.append(x)
    return color_list

#creating variables differentiating input and similar track features's colors
i_color_code = color_code(i_features)
o_color_code = color_code(o_features)

#creating variables differentiating input and similar BPM's colors
bpm_color_list_i = [(0,0,i_features[4]), (0, i_features[4],0), (i_features[4], 0, 0)]
bpm_color_list_o = [(0,0,o_features[4]), (0, o_features[4],0), (o_features[4], 0, 0)]

class Record:
    """
    Class to keep track of a record's location + vector
    """
    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0

def make_record():
    '''
    function to make moving records for background
    '''
    record = Record()
    #position of outer
    record.x = random.randrange(record_size, screen_width-record_size)
    record.y = random.randrange(record_size, screen_height-record_size)
    #speed and direction of recrod
    record.dx = random.randrange(-2,2)
    record.dy = random.randrange(-2,2)
    record.color = color_list[0]

    return record

def main():
    """
    main program
    """
    pygame.init()
    pygame.font.init()
    #initializing screen
    size = [screen_width, screen_height]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("MUSIC JUNKIE")

    #looping until close button is clicked
    done = False

    #used to manage how fast screen updates
    clock = pygame.time.Clock()

    #number of records initially
    record_list = []

    for i in range(random.randrange(2,10)):
        record = make_record()
        record_list.append(record)


    """
    main loop
    """
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #space bar makes new record
                    record = make_record()
                    record_list.append(record)

        for record in record_list:
            #movement
            record.x += record.dx
            record.y += record.dy

            #screen bounce
            if record.y > screen_height-record_size or record.y < record_size:
                record.dy *= -1
                record.color = color_list[random.randrange(0, len(color_list)-1)]

            if record.x > screen_width-record_size or record.x < record_size:
                record.dx *= -1
                record.color = color_list[random.randrange(0, len(color_list)-1)]
        #setting screen background
        screen.fill(grey)

        #draw record with scaling to record size
        for record in record_list:
            pygame.draw.circle(screen, black, (record.x, record.y), record_size)
            pygame.draw.circle(screen, record.color, (record.x, record.y), record_size-int(record_size/2))
            pygame.draw.circle(screen, white, (record.x, record.y), record_size-int(0.75*record_size))

        #transparent overlay
        s = pygame.Surface((screen_width,screen_height))  # the size of your rect
        s.set_alpha(100)                # alpha level
        s.fill((255,255,255))           # this fills the entire surface
        screen.blit(s, (0,0))    # (0,0) are the top-left coordinates

        #setting font
        font = 'tlwgtypewriter'
        bigfont = pygame.font.SysFont(font, 40)
        myfont = pygame.font.SysFont(font, 18)
        smallfont = pygame.font.SysFont(font, 15)
        medfont = pygame.font.SysFont(font, 25)

        #creating BPM art
        pygame.draw.rect(screen,random.choice(bpm_color_list_i), (100,300, 230,230),0 )
        pygame.draw.rect(screen,random.choice(bpm_color_list_o), (520,300, 230,230),0 )

        #make title
        pygame.draw.rect(screen, black, (20, 20, screen_width-40,screen_height/8), 0)
        pygame.draw.rect(screen, brightred, (30, 30, screen_width-60,screen_height/8-20), 4)
        title = bigfont.render('| J.CHILLIN MUSIC TRANSCENDER |', True, white)
        screen.blit(title, (56, 50))

        #track features label
        pygame.draw.rect(screen, black, (250, 584, 330, 45), 0)
        ins_title_tf = myfont.render('T R A C K  F E A T U R E S', True, brightgreen)
        screen.blit(ins_title_tf, (270, 594))
        '''
        INITIAL SONG LABELING
        '''
        #labeling: initial song
        x_justify = 35
        pygame.draw.rect(screen, black, (x_justify + 80, 145, 205,33), 0)
        ins_title = myfont.render('O R I G I N A L', False, steelblue)
        screen.blit(ins_title, (x_justify + 100, 150))

        pygame.draw.rect(screen, steelblue, (x_justify - 10, 180, 385, 100), 3)
        ins_track = smallfont.render('T R A C K: ' + i_general[0], True, white)
        screen.blit(ins_track, (x_justify, 190))

        ins_artist = smallfont.render('A R T I S T: ' + i_general[1], True, white)
        screen.blit(ins_artist, (x_justify, 220))

        ins_album = smallfont.render('A L B U M: ' + i_general[2] + "(" + i_general[3] + ")", True, white)
        screen.blit(ins_album, (x_justify, 250))

        #track features: initial
        pygame.draw.rect(screen, steelblue, (x_justify - 10, 630, 385, 205), 3)

        ins_mode = myfont.render('MODE: ' + i_features[0], True, i_color_code[0])
        screen.blit(ins_mode, (x_justify, 640))

        ins_key = myfont.render('KEY: ' + i_features[1], True, i_color_code[1])
        screen.blit(ins_key, (x_justify, 680))

        ins_danceability = myfont.render('DANCE LEVEL: ' + i_features[2], True, i_color_code[2])
        screen.blit(ins_danceability, (x_justify, 720))

        ins_energy = myfont.render('ENERGY: ' + i_features[3], True, i_color_code[3])
        screen.blit(ins_energy, (x_justify, 760))

        ins_bpm = myfont.render('BPM ART: ' + str(i_features[4]), True, i_color_code[4])
        screen.blit(ins_bpm, (x_justify + 115, 540))

        ins_valence = myfont.render('FEELING: ' + i_features[5], True, i_color_code[5])
        screen.blit(ins_valence, (x_justify, 800))

        '''
        OUTPUT SONG LABELING
        '''
        #labeling: output song
        y_justify = 450
        pygame.draw.rect(screen, black, (y_justify + 90, 145, 180,33), 0)

        out_title = myfont.render('S I M I L A R', False, steelblue)
        screen.blit(out_title, (y_justify+110, 150))

        pygame.draw.rect(screen, steelblue, (y_justify - 10, 180, 385, 100), 3)

        out_track = smallfont.render('T R A C K: ' + o_general[0], True, white)
        screen.blit(out_track, (y_justify, 190))

        out_artist = smallfont.render('A R T I S T: ' + o_general[1], True, white)
        screen.blit(out_artist, (y_justify, 220))

        out_album = smallfont.render('A L B U M: ' + o_general[2] + '(' + o_general[3] + ')', True, white)
        screen.blit(out_album, (y_justify, 250))

        #track features: output
        pygame.draw.rect(screen, steelblue, (y_justify - 10, 630, 385, 205), 3)

        out_mode = myfont.render('MODE: ' + o_features[0], True, o_color_code[0])
        screen.blit(out_mode, (y_justify, 640))

        out_key = myfont.render('KEY: ' + o_features[1], True, o_color_code[1])
        screen.blit(out_key, (y_justify, 680))

        out_danceability = myfont.render('DANCE LEVEL: ' + o_features[2], True, o_color_code[2])
        screen.blit(out_danceability, (y_justify, 720))

        out_energy = myfont.render('ENERGY: ' + o_features[3], True, o_color_code[3])
        screen.blit(out_energy, (y_justify, 760))

        out_bpm = myfont.render('BPM ART: ' + str(o_features[4]), True, o_color_code[4])
        screen.blit(out_bpm, (y_justify + 120, 540))

        out_valence = myfont.render('FEELING: ' + o_features[5], True, o_color_code[5])
        screen.blit(out_valence, (y_justify, 800))

        #creds
        thanks = myfont.render('M A D E  B Y:  A N N I E  C H U  +  N I C K  B O U R D O N', True, white)
        screen.blit(thanks, (100, screen_height-40))

        #limiting 60 frames per second
        clock.tick(30)

        #updating screen
        pygame.display.flip()

    #closing down
    pygame.quit()

if __name__ == "__main__":
    main()
