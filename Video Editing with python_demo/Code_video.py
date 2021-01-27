from moviepy.editor import VideoFileClip, CompositeVideoClip, concatenate_videoclips, clips_array
import moviepy.video.fx.all as vfx

##The videos from where the final video and sub videos are derived
trailer=VideoFileClip("trailer.mp4", audio=False)   ##this is the first video clip
trailer2=VideoFileClip("trailer2.mp4", audio=False) ## this is the second video clip

############## stage1 of the video, introducing attacks and the mission
Mastermind=trailer2.subclip(73.11, 75.39)           ## This is the clip showing a masked man
Mastermind=vfx.time_mirror(Mastermind)              ## using vfx effect- time mirror
mah, mah= Mastermind.size
##clip's size changed, with height reduced to half 
Mastermind=Mastermind.crop(width=mah, height=mah/2, x_center=mah/2, y_center=mah/2)
Mastermind=Mastermind.set_start(1)                  ## clip starts after 1 second

Delhi=trailer2.subclip(61.86, 62.85)                ## clip showing attack of Delhi
dw, dh = Delhi.size
##clip's size changed, with height changed to half the height of clip named Mastermind
Delhi = Delhi.crop(width=dw, height=mah/2, x_center=dw/2, y_center=dh/2)

Mumbai1=trailer2.subclip(63.84, 64.84)              ##clip showing attack of Mumbai 2006
Mumbai2=trailer2.subclip(65.13, 66.84)              ##clip showing attack of Mumbai 2008
mh, mw = Mumbai1.size
##clips Mumbai1's and Mumbai2's size changed, with height changed to half the height of clip named Mastermind
Mumbai1=Mumbai1.crop(width=mh, height=mah/2, x_center=mh/2, y_center=mw/2)
Mumbai2=Mumbai2.crop(width=mh, height=mah/2, x_center=mh/2, y_center=mw/2)

Kashmir=trailer2.subclip(67.12, 69.12)              ##clip showing attack of Kashmir
kh, kw= Kashmir.size
##clip's size changed, with height changed to half the height of clip named Mastermind
Kashmir=Kashmir.crop(width=kh, height=mah/2, x_center=kh/2, y_center=kw/2)

Hunt=trailer2.subclip(77.10, 78.24)                 ##clip showing the words "19 years Manhunt", used as a background 
Hunt=vfx.freeze(Hunt, 0, 3)                         ##vfx effect- freeze video for the first 3 seconds
Hunt=vfx.fadeout(Hunt, 1)                           ## vfx effect- video fades out in the last one second
huntw, hunth=Hunt.size
##clip's size changed, with height reduced by 100 units
Hunt=Hunt.crop(width=huntw, height=hunth-100, x_center=huntw/2, y_center=hunth/2)

##resize video clips to avoid overlapping completely upon composition
Delhi=Delhi.resize(0.5) 
Mumbai1=Mumbai1.resize(0.5)
Mumbai2=Mumbai2.resize(0.5)
Kashmir=Kashmir.resize(0.5)
Mastermind=Mastermind.resize(0.6) 

Delhi=Delhi.set_position(("left", "top"))           ##position of clip- top left corner
Mumbai1=Mumbai1.set_position(("right", "top"))      ##position of clip- top right corner
Mumbai2=Mumbai2.set_position(("right", "bottom"))   ##position of clip- bottom right corner
Kashmir=Kashmir.set_position(("left", "bottom"))    ##position of clip- bottom left corner
Mastermind=Mastermind.set_position("center")        ##position of clip- center

##composite of video clips- Hunt, Delhi, Mumbai1, Mumbai2, Kashmir, Mastermind,
##with Hunt being treated as background video for the time being
##composite video saved to final1
final1=CompositeVideoClip([Hunt, Delhi, Mumbai1, Mumbai2, Kashmir, Mastermind])  

#################################################################################

######################Intro of analyst Himmat, stage2 of video

Himmat1=trailer2.subclip(97,98)
Himmat2=trailer2.subclip(100.38,102.90)

##video clips Himmat1 and Himmat2 being concatenated 
final2 = concatenate_videoclips([Himmat1, Himmat2], method="compose")
himw, himh = final2.size
##concatenated video is resized, with reduction in height, saved again in final2
final2 = final2.crop(width=himw, height=himh-80, x_center=himw/2, y_center=himh/2)

##############################################################################

############for the stage3 where 5 agents are introduced, stack effect is used

Farooq=trailer.subclip(46,49)                       ##agent Farooq introduced
faw, fah = Farooq.size
##clip Farooq resized, height and width reduced to half
Farooq = Farooq.crop(width=faw/2, height=fah/2, x_center=faw/2, y_center=fah/2)

Ruhani=trailer.subclip(83.13,86.13)                 ##agent Ruhani introduced
rw, rh = Ruhani.size
##clip Ruhani resized, height and width reduced to half
Ruhani = Ruhani.crop(width=rw/2, height=rh/2, x_center=rw/2, y_center=rh/2)

Avinash=trailer.subclip(86.66,89.66)                ##agent Avinash introduced
aw, ah = Avinash.size
##clip Avinash resized, height and width reduced to half
Avinash = Avinash.crop(width=aw/2, height=ah/2, x_center=aw/2, y_center=ah/2)

Juhi=trailer.subclip(91,94)                         ##agent Juhi introduced
jw, jh = Juhi.size
##clip Juhi resized, height and width reduced to half
Juhi = Juhi.crop(width=jw/2, height=jh/2, x_center=jw/2, y_center=jh/2)

Bala=trailer.subclip(94.43,97.43)                   ##agent Bala introduced
bw, bh = Bala.size
##clip Bala resized, height and width reduced to half
Bala = Bala.crop(width=bw/2, height=bh/2, x_center=bw/2, y_center=bh/2)

NumberAgents=trailer2.subclip(84,85)                ##clip showing number of countries and agents

##clip freezed at its first second for 2 seconds, while showing number of agents
freeze = vfx.freeze(NumberAgents, 1.0, 2.0) 
fw, fh = freeze.size
##clip's size changed, with height reduced by 80 units
freeze = freeze.crop(width=fw, height=fh-80, x_center=fw/2, y_center=fh/2) 
freeze=freeze.resize(0.5)                           ## clip again resized

##stack of video clips- Farooq, freeze, Ruhani,Juhi, Avinash, Bala,
##video clips are placed in the order as written in the code- 3*3,
##[Farooq, freeze, Ruhani]- on top, below-[Juhi, Avinash, Bala],
##composite video saved to final3
final3= clips_array([[Farooq, freeze, Ruhani],[Juhi, Avinash, Bala],])

#############################################################################

####################### Introduction of Hafiz, stage4

Hafiz1=trailer2.subclip(89.31,90.50)
Hafiz1=vfx.invert_colors(Hafiz1)                    ##vfx effect- inversion of colors, to give a suspicious look
Hafiz2=trailer.subclip(122.71, 123.41)          
Hafiz3=trailer.subclip(78.02, 78.85)

##clips Hafiz1, Hafiz2, Hafiz3 concatenated and saved to Hafiz, to introduce Hafiz
Hafiz=concatenate_videoclips([Hafiz1,Hafiz2, Hafiz3], method="compose")
hafw,hafh= Hafiz1.size
##size of clip changed, with height reduced to half
Hafiz=Hafiz.crop(width=hafw, height=hafh/2, x_center=hafw/2, y_center=hafh/2)
Hafiz=vfx.freeze(Hafiz, 0, 2)                       ##vfx effect- freeze at 0th second for 2 seconds

Lead=trailer.subclip(43.84, 44.84)                  ##clip to introduce the leader initiating operation
leadw, leadh= Lead.size
##size of clip changed, with height reduced by 100 units
Lead=Lead.crop(width=leadw, height=leadh-100, x_center=leadw/2, y_center=leadh/2)
Lead=Lead.resize(0.4)                               ##resize video clip to avoid overlapping completely upon composition
Lead=Lead.set_position(("right", "bottom"))         ##clip is placed on bottom right corner

Team=trailer2.subclip(98.90,99.90)                  ##clip to show the team handling the operation
teamw, teamh= Team.size
##size of clip changed, with height reduced by 100 units
Team=Team.crop(width=teamw, height=teamh-100, x_center=teamw/2, y_center=teamh/2)
Team=Team.resize(0.4)                               ##resize video clip to avoid overlapping completely upon composition
Team=Team.set_position(("left", "bottom"))          ##clip is placed on bottom left corner of the video

##composition of video clips Hafiz, Team and Lead,
##with the clip named Hafiz being used as background
final4=CompositeVideoClip([Hafiz, Team, Lead])

#########################################################################################

################### ending of the video

Ending=trailer.subclip(135, 138)                    ##ending clip of the video
Ending=vfx.fadein(Ending,2)                         ##vfx effects- clip fades in its last two seconds
endw, endh= Ending.size
##size of clip changed and saved to final5
##height reduced by 100 units
final5 = Ending.crop(width=endw, height=endh-100, x_center=endw/2, y_center=endh/2)

#########################################################################################

######################concatenate all stages-

final3.resize(0.2)                                 ## resizing the stack video, as it is larger, to achieve successful concatenation

##clips final1, final2, final3, final4, final5 being concatenated in this order,
##and saved in this order
final = concatenate_videoclips([final1, final2, final3, final4, final5], method="compose")
final.write_videofile("finalVideo2.mp4")            ##the video is written to- finalVideo2.mp4

##########################################################################################
