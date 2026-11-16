import maya.cmds as cmds
import random

def create_animation(
    timing_spin,
    step_spin,
    translate_spin_minx,
    translate_spin_miny,
    translate_spin_minz,
    translate_spin_maxx,
    translate_spin_maxy,
    translate_spin_maxz,
    rotate_spin_minx,
    rotate_spin_miny,
    rotate_spin_minz,
    rotate_spin_maxx,
    rotate_spin_maxy,
    rotate_spin_maxz,
    scale_spin_minx,
    scale_spin_miny,
    scale_spin_minz,
    scale_spin_maxx,
    scale_spin_maxy,
    scale_spin_maxz
):
    selected_obj = cmds.ls(selection=True, objectsOnly=True) # get tous les objets sélectionnés

    # reset la timeline pour loop mon animation
    cmds.currentTime(1)
    cmds.playbackOptions(minTime=1, maxTime=timing_spin)
    cmds.playbackOptions(animationStartTime=1, animationEndTime=timing_spin)

    steps_add = 0
    midsteps = []

    # ajoute les frames ou placer des keys selon le step choisi
    while(steps_add < timing_spin - step_spin):
        steps_add += step_spin
        midsteps.append(steps_add)

    cmds.undoInfo(closeChunk=True) # ctrl z -----------------------
    cmds.undoInfo(openChunk=True) 

    for i in selected_obj:

        # reset les clés d'animations
        cmds.cutKey(i, clear=True)

        # --- set frame 1 keys ---
        # get la position initiale
        init_positionX = cmds.getAttr(i + ".translateX")
        init_positionY = cmds.getAttr(i + ".translateY")
        init_positionZ = cmds.getAttr(i + ".translateZ")
        init_rotationX = cmds.getAttr(i + ".rotateX")
        init_rotationY = cmds.getAttr(i + ".rotateY")
        init_rotationZ = cmds.getAttr(i + ".rotateZ")
        init_scaleX = cmds.getAttr(i + ".scaleX")
        init_scaleY = cmds.getAttr(i + ".scaleY")
        init_scaleZ = cmds.getAttr(i + ".scaleZ")

        #set la 1ere et derniere comme les transformations initiales de l'objet
        for frame in [1, timing_spin]:
            cmds.setKeyframe(i, attribute="translateX", time=frame, value=init_positionX)
            cmds.setKeyframe(i, attribute="translateY", time=frame, value=init_positionY)
            cmds.setKeyframe(i, attribute="translateZ", time=frame, value=init_positionZ)
            cmds.setKeyframe(i, attribute="rotateX", time=frame, value=init_rotationX)
            cmds.setKeyframe(i, attribute="rotateY", time=frame, value=init_rotationY)
            cmds.setKeyframe(i, attribute="rotateZ", time=frame, value=init_rotationZ)
            cmds.setKeyframe(i, attribute="scaleX", time=frame, value=init_scaleX)
            cmds.setKeyframe(i, attribute="scaleY", time=frame, value=init_scaleY)
            cmds.setKeyframe(i, attribute="scaleZ", time=frame, value=init_scaleZ)

        for frame in midsteps:
            cmds.setKeyframe(i, attribute="translateX", time=frame, value=random.randrange(translate_spin_minx, translate_spin_maxx))
            cmds.setKeyframe(i, attribute="translateY", time=frame, value=random.randrange(translate_spin_miny, translate_spin_maxy))
            cmds.setKeyframe(i, attribute="translateZ", time=frame, value=random.randrange(translate_spin_minz, translate_spin_maxz))
            cmds.setKeyframe(i, attribute="rotateX", time=frame, value=random.randrange(rotate_spin_minx, rotate_spin_maxx))
            cmds.setKeyframe(i, attribute="rotateY", time=frame, value=random.randrange(rotate_spin_miny, rotate_spin_maxy))
            cmds.setKeyframe(i, attribute="rotateZ", time=frame, value=random.randrange(rotate_spin_minz, rotate_spin_maxz))
            cmds.setKeyframe(i, attribute="scaleX", time=frame, value=random.randrange(scale_spin_minx, scale_spin_maxx))
            cmds.setKeyframe(i, attribute="scaleY", time=frame, value=random.randrange(scale_spin_miny, scale_spin_maxy))
            cmds.setKeyframe(i, attribute="scaleZ", time=frame, value=random.randrange(scale_spin_minz, scale_spin_maxz))

    cmds.undoInfo(closeChunk=True) # ctrl z -------------------------------
