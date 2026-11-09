# Design Doc Critique:

Almost all changes were good, pointing out various inconsistencies. 

The need to mention that data is removed in the kiosk fallbacks in failure states is important. It is essential to ensure that any data that might have been stored mid-transaction, such as card or user info, is removed upon failure. This is essential to fulfill the security NFR.

I did disagree somewhat with the way it approached the payment authorization. It seemed to suggest modifying the executeCharge() interface, but in my opinion it would probably be better to simply define a different interface alltogether for this purpose. 

It also feels somewhat redundant to include methods for handling cash payments in BOTH Employee and Order. This would probably be better as a simple "fulfill_transaction" method in Employee to mark the order as paid. Then they do the cash stuff manually.