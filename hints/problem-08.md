1. Find the two "hash"-es that we use to compare if the system is in sync or not.
2. Check how we calculate those. Do we filter correctly
3. Once you have two real hashes compare them. If the difference is more than 1 second check the note at the end.
4. Check when we calculate them (before or after reading from the database)


NOTE: During the workshop we found out that a Windows machine produced a 2 hours difference between the two timestamps. This was not an intended bug, but you can still play a bit and see who to fix it.

