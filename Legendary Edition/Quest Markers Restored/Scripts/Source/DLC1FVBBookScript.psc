Scriptname DLC1FVBBookScript extends ReferenceAlias  

Quest Property pDLC1VQFVBooks Auto
GlobalVariable Property pDLC1FVBGotABook Auto
GlobalVariable Property pDLC1FVBBooksDiscovered Auto

Event OnContainerChanged(ObjectReference akNewContainer, ObjectReference akOldContainer)
	If akNewContainer == Game.GetPlayer()
		pDLC1FVBGotABook.Mod(1.0)
		pDLC1VQFVBooks.ModObjectiveGlobal(1.0, pDLC1FVBBooksDiscovered, 8, 4.0)
		If pDLC1FVBBooksDiscovered.GetValue() >= 4.0
			pDLC1VQFVBooks.SetStage(20)
		EndIf
	EndIf
EndEvent
