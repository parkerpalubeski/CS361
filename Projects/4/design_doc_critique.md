# Design Doc Critique:
Despite me trying multiple times with multiple models, they changed remarkably little between the my document and their's which didn't leave me much to work with.

## In Constraints:
+  Reservation modifications made outside of a 24-hour cutoff window incur no penalty fees
This was one that was covered in Rodney's requirements gathering and subsequently appeared in one of my user stories, but that I missed while creating the design doc. Because of this I believe this is one that is worth keeping.

## In Components:
I believe the addition of a reservation manager to handle 24-hour cancellation cutoff windows isn't really necessary. It essentially is a part of the Rental Logic Unit anyways, and would only really be kept separate as part of separation of concerns, even though its logic is heavily tied to RLU. I believe this doesn't need to be on the design doc at least since its separation is mostly implied.

## Seasonal Rate Adjustments
This was another one that I missed which actually appeared in the original requirements back in project 1. I don't believe Rodney specifically mentioned what the rate adjustments are, so the way the AI kept it as a "manual" thing that is performed in the admin portal is something I agree with. That way he can adjust them as he likes.