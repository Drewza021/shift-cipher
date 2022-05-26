# Shift Cipher
<p><strong>Shift cipher program developed in Python capable of encryption and decryption</strong></p>
<p>Shifts according to character positions in seperate strings of letters, numbers, and special characters located on US keyboard.  Letter case is retained.</p>
<h2>Encryption</h2><br>
<p>User inputted message and key generates ciphertext.  Key determines number of positions forward or backward new character is set to.</p>
<h2>Decryption</h2>
<p>User may choose key based decryption or cryptanalysis (automatic, doesn't require key).  Key based decryption algorithm works same as encryption algorithm however backwards, with guarantee of successful decryption provided that the key is correct.  Cryptanalysis uses letter frequency analysis to determine 5 most likely possible messages.  User may execute brute force decryption to show all 26 possible messages in the case that this is not successful.</p>
<p><b>Only 100% effective if ciphertext was generated with this same program.</b></p>
<h2>Additional</h2>
<p><b>Requires Python to be interpreted and executed.</b>  Included frequency analyser tool was created for debugging purposes during development, and has been included in repo because why not?  This returns frequencies of characters within a user inputted string, ordered most to least frequent.
