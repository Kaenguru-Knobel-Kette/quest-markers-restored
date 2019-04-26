ScriptName TT_NN01CrimsonNirnrootScript Extends ReferenceAlias



Event OnActivate(ObjectReference akActionRef)
	If (akActionRef == Game.GetPlayer())
		Clear()
	EndIf
EndEvent
