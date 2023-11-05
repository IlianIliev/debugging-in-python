1. To reproduce the issue try the following:
   1. Create a new account by passing custom `profile_header`
   2. Create another account with empty `profile_header`
   3. The second account should have inherited the `profile_header` of the first
2. Python has mutable and immutable types. You should be extra careful when using the first.  
3. This one is trickier as you have to fix it in two places. 
