#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Juli 26, 2022, at 13:06
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'ratings'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='C:\\Users\\Sophie\\Documents\\BP\\Versuch\\para\\training\\training_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "intro"
introClock = core.Clock()
intro_text = visual.TextStim(win=win, name='intro_text',
    text='Welcome!\n\nPlease look at the following images\nand rate them according to\nhow you feel about them.\n\n[Click anywhere to continue...]\n',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
intro_mouse = event.Mouse(win=win)
x, y = [None, None]
intro_mouse.mouseClock = core.Clock()
from pylsl import StreamInfo, StreamOutlet


# Setup the LSL stream
info = StreamInfo(name='PsychoPy', type='Markers', channel_count=1,
                  channel_format='string', source_id='PsychopyMarkersID321654')

# Initialize the LSL stream.
outlet = StreamOutlet(info)

# Initialize components for Routine "pre"
preClock = core.Clock()
pre_text = visual.TextStim(win=win, name='pre_text',
    text='Get ready...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "fix"
fixClock = core.Clock()
fixation_cross = visual.ShapeStim(
    win=win, name='fixation_cross', vertices='cross',
    size=(0.05, 0.08),
    ori=0, pos=(0, 0), anchor='center',
    lineWidth=1,     colorSpace='rgb',  lineColor=[1,1,1], fillColor=[1,1,1],
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "blank"
blankClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "image"
imageClock = core.Clock()
stim_image = visual.ImageStim(
    win=win,
    name='stim_image', 
    image='sin', mask=None, anchor='center',
    ori=0, pos=(0, 0), size=(1, 1.5),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "rating"
ratingClock = core.Clock()
valence = visual.ImageStim(
    win=win,
    name='valence', 
    image='img/SAM-V-9.png', mask=None, anchor='center',
    ori=0.0, pos=(0, 0.5), size=(1.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
arousal1 = visual.ImageStim(
    win=win,
    name='arousal1', 
    image='img/SAM-A-9.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.4), size=(1.5, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)
val_slider = visual.Slider(win=win, name='val_slider',
    startValue=None, size=(1.28, 0.1), pos=(0, 0.2), units=None,
    labels=None, ticks=(-4, -3, -2, -1, 0, 1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-2, readOnly=False)
ar_slider = visual.Slider(win=win, name='ar_slider',
    startValue=None, size=(1.28, 0.1), pos=(0, -0.7), units=None,
    labels=None, ticks=(-4, -3, -2, -1, 0, 1, 2, 3, 4), granularity=0.0,
    style='rating', styleTweaks=(), opacity=None,
    labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-3, readOnly=False)

# Initialize components for Routine "end"
endClock = core.Clock()
end_text = visual.TextStim(win=win, name='end_text',
    text='"""\nThanks for your participation!\n"""',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "intro"-------
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the intro_mouse
gotValidClick = False  # until a click is received
outlet.push_sample(["intro"])
# keep track of which components have finished
introComponents = [intro_text, intro_mouse]
for thisComponent in introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "intro"-------
while continueRoutine:
    # get current time
    t = introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *intro_text* updates
    if intro_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_text.frameNStart = frameN  # exact frame index
        intro_text.tStart = t  # local t and not account for scr refresh
        intro_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_text, 'tStartRefresh')  # time at next scr refresh
        intro_text.setAutoDraw(True)
    # *intro_mouse* updates
    if intro_mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        intro_mouse.frameNStart = frameN  # exact frame index
        intro_mouse.tStart = t  # local t and not account for scr refresh
        intro_mouse.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(intro_mouse, 'tStartRefresh')  # time at next scr refresh
        intro_mouse.status = STARTED
        intro_mouse.mouseClock.reset()
        prevButtonState = intro_mouse.getPressed()  # if button is down already this ISN'T a new click
    if intro_mouse.status == STARTED:  # only update if started and not finished!
        buttons = intro_mouse.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                continueRoutine = False  # abort routine on response    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "intro"-------
for thisComponent in introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('intro_text.started', intro_text.tStartRefresh)
thisExp.addData('intro_text.stopped', intro_text.tStopRefresh)
# store data for thisExp (ExperimentHandler)
x, y = intro_mouse.getPos()
buttons = intro_mouse.getPressed()
thisExp.addData('intro_mouse.x', x)
thisExp.addData('intro_mouse.y', y)
thisExp.addData('intro_mouse.leftButton', buttons[0])
thisExp.addData('intro_mouse.midButton', buttons[1])
thisExp.addData('intro_mouse.rightButton', buttons[2])
thisExp.addData('intro_mouse.started', intro_mouse.tStart)
thisExp.addData('intro_mouse.stopped', intro_mouse.tStop)
thisExp.nextEntry()
# the Routine "intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "pre"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
preComponents = [pre_text]
for thisComponent in preComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
preClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "pre"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = preClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=preClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *pre_text* updates
    if pre_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        pre_text.frameNStart = frameN  # exact frame index
        pre_text.tStart = t  # local t and not account for scr refresh
        pre_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(pre_text, 'tStartRefresh')  # time at next scr refresh
        pre_text.setAutoDraw(True)
    if pre_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > pre_text.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            pre_text.tStop = t  # not accounting for scr refresh
            pre_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(pre_text, 'tStopRefresh')  # time at next scr refresh
            pre_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in preComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "pre"-------
for thisComponent in preComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('pre_text.started', pre_text.tStartRefresh)
thisExp.addData('pre_text.stopped', pre_text.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('lists/img2_training.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "fix"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    fixComponents = [fixation_cross]
    for thisComponent in fixComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "fix"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = fixClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=fixClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *fixation_cross* updates
        if fixation_cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            fixation_cross.frameNStart = frameN  # exact frame index
            fixation_cross.tStart = t  # local t and not account for scr refresh
            fixation_cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(fixation_cross, 'tStartRefresh')  # time at next scr refresh
            fixation_cross.setAutoDraw(True)
        if fixation_cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > fixation_cross.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                fixation_cross.tStop = t  # not accounting for scr refresh
                fixation_cross.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation_cross, 'tStopRefresh')  # time at next scr refresh
                fixation_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in fixComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "fix"-------
    for thisComponent in fixComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('fixation_cross.started', fixation_cross.tStartRefresh)
    trials.addData('fixation_cross.stopped', fixation_cross.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [text]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    blankClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=blankClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + .5-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text.started', text.tStartRefresh)
    trials.addData('text.stopped', text.tStopRefresh)
    
    # ------Prepare to start Routine "image"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    stim_image.setImage(f"./img/{img_name}")
    outlet.push_sample([img_name])
    # keep track of which components have finished
    imageComponents = [stim_image]
    for thisComponent in imageComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    imageClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "image"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = imageClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=imageClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim_image* updates
        if stim_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            stim_image.frameNStart = frameN  # exact frame index
            stim_image.tStart = t  # local t and not account for scr refresh
            stim_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim_image, 'tStartRefresh')  # time at next scr refresh
            stim_image.setAutoDraw(True)
        if stim_image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > stim_image.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                stim_image.tStop = t  # not accounting for scr refresh
                stim_image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(stim_image, 'tStopRefresh')  # time at next scr refresh
                stim_image.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in imageComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "image"-------
    for thisComponent in imageComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('stim_image.started', stim_image.tStartRefresh)
    trials.addData('stim_image.stopped', stim_image.tStopRefresh)
    
    # ------Prepare to start Routine "rating"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    val_slider.reset()
    ar_slider.reset()
    # keep track of which components have finished
    ratingComponents = [valence, arousal1, val_slider, ar_slider]
    for thisComponent in ratingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ratingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rating"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ratingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ratingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *valence* updates
        if valence.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            valence.frameNStart = frameN  # exact frame index
            valence.tStart = t  # local t and not account for scr refresh
            valence.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(valence, 'tStartRefresh')  # time at next scr refresh
            valence.setAutoDraw(True)
        if valence.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > valence.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                valence.tStop = t  # not accounting for scr refresh
                valence.frameNStop = frameN  # exact frame index
                win.timeOnFlip(valence, 'tStopRefresh')  # time at next scr refresh
                valence.setAutoDraw(False)
        
        # *arousal1* updates
        if arousal1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arousal1.frameNStart = frameN  # exact frame index
            arousal1.tStart = t  # local t and not account for scr refresh
            arousal1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arousal1, 'tStartRefresh')  # time at next scr refresh
            arousal1.setAutoDraw(True)
        if arousal1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > arousal1.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                arousal1.tStop = t  # not accounting for scr refresh
                arousal1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(arousal1, 'tStopRefresh')  # time at next scr refresh
                arousal1.setAutoDraw(False)
        
        # *val_slider* updates
        if val_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            val_slider.frameNStart = frameN  # exact frame index
            val_slider.tStart = t  # local t and not account for scr refresh
            val_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(val_slider, 'tStartRefresh')  # time at next scr refresh
            val_slider.setAutoDraw(True)
        if val_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > val_slider.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                val_slider.tStop = t  # not accounting for scr refresh
                val_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(val_slider, 'tStopRefresh')  # time at next scr refresh
                val_slider.setAutoDraw(False)
        
        # *ar_slider* updates
        if ar_slider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ar_slider.frameNStart = frameN  # exact frame index
            ar_slider.tStart = t  # local t and not account for scr refresh
            ar_slider.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ar_slider, 'tStartRefresh')  # time at next scr refresh
            ar_slider.setAutoDraw(True)
        if ar_slider.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > ar_slider.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                ar_slider.tStop = t  # not accounting for scr refresh
                ar_slider.frameNStop = frameN  # exact frame index
                win.timeOnFlip(ar_slider, 'tStopRefresh')  # time at next scr refresh
                ar_slider.setAutoDraw(False)
        
        # Check ar_slider for response to end routine
        if ar_slider.getRating() is not None and ar_slider.status == STARTED:
            continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ratingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rating"-------
    for thisComponent in ratingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('valence.started', valence.tStartRefresh)
    trials.addData('valence.stopped', valence.tStopRefresh)
    trials.addData('arousal1.started', arousal1.tStartRefresh)
    trials.addData('arousal1.stopped', arousal1.tStopRefresh)
    trials.addData('val_slider.response', val_slider.getRating())
    trials.addData('val_slider.rt', val_slider.getRT())
    trials.addData('val_slider.started', val_slider.tStartRefresh)
    trials.addData('val_slider.stopped', val_slider.tStopRefresh)
    trials.addData('ar_slider.response', ar_slider.getRating())
    trials.addData('ar_slider.rt', ar_slider.getRT())
    trials.addData('ar_slider.started', ar_slider.tStartRefresh)
    trials.addData('ar_slider.stopped', ar_slider.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


# ------Prepare to start Routine "end"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
# keep track of which components have finished
endComponents = [end_text]
for thisComponent in endComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "end"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = endClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *end_text* updates
    if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_text.frameNStart = frameN  # exact frame index
        end_text.tStart = t  # local t and not account for scr refresh
        end_text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
        end_text.setAutoDraw(True)
    if end_text.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > end_text.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            end_text.tStop = t  # not accounting for scr refresh
            end_text.frameNStop = frameN  # exact frame index
            win.timeOnFlip(end_text, 'tStopRefresh')  # time at next scr refresh
            end_text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "end"-------
for thisComponent in endComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('end_text.started', end_text.tStartRefresh)
thisExp.addData('end_text.stopped', end_text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
