# Shufflelith
*Before I go any further, I should explain that this is my first time creating a repository in GitHub, and have extremely limited coding knowledge. So I will be explaining the instructions
as if I were describing them to myself. Forgive me if some of what I say is redundant, but I prefer being overly clear if it means more accessibility to non-nerds like myself.*

This program is a Python script to allow the user to decide which biomes they want from Terralith and Minecraft. It runs in the command line, because I do not know how to create an EXE. Sorry, smelly nerds.

Anyways, the setup is fairly simple. Download the Terralith mod (a jar file), and extract its contents using something like 7Zip or BreeZip. Navigate inside the unzipped Terralith folder through the following path
Terralith (folder) > data > minecraft > dimension   

Inside the dimension folder, copy/cut the overworld.json file and place move it into the same folder/location as the Python script you'll download, likely in your downloads folder.

From there, open the command line to the directory that contains Shuffelith.py and overworld.json, likely your C:\users\YOU\downloads>
With the terminal open, run the following command: `python Shufflelith.py`

The interface will prompt you on how you want to categorize your biomes. Let me take a brief detour and describe what the hell this means
The prompt of categorizing biomes essentially means grouping all biomes of a similar type and later allowing you to determine what you want to replace those specific biomes
For example, you select Beach. This groups all Beach type biomes, like minecraft:beach, terralith:gravel_beach etc into one group.
In the next stage, you can say that you want these Beach grouped biomes to be replaced with minecraft:lush_caves, just to throw out a biome. 

The first 4 categories are fairly self explanatory, but let me explain the next 3.
Skylands: Due to how Terralith generates, you can only replace Skyland biomes with other skyland biomes or other ocean biomes
All Remaining Biomes: This is sequentially the final non-aquatic biome generation, it basically selects all biomes not previously grouped under "Beach" or "Desert", and groups them all
    If you select just this, this will affect every single non-aquatic biome. Finish the readme before selecting this option
Ocean: Due to how Minecraft generates, you can only replace ocean biomes with other ocean biomes or skylands biomes

Next it will prompt you for which biomes you want included in each category. This is a list of every terralith and minecraft surface biome (and lush caves because I like them on the surface)
Note that the more biomes you include in each category makes each biome rarer respectively.
**The more biomes you select for the "All Remaining Biomes" category, the more chaotic the world will be. Each biome has even weighting and thus the more biomes included, the smaller biomes get and more random it is**

Once you are finished with each category selection, Shuffelith will generate a file named RENAME.json to avoid overwriting the overworld.json file. **The next steps are crucial to ensure Terralith can read the new file properly.**

Take RENAME.json and move it into the dimension folder in Terralith in the path described above. Once it is placed here, rename it to overworld.json
Then, exit to the first level inside the Terralith folder, you should see files like license.txt, various folders, fabric.mod.json
Select **everything** in the Terralith folder, including all the folders and text files you see, right click and compress to zip. Name the first part something identifying, and then **change the file to have a .jar ending, not a .zip.** A warning will pop up, but click Yes and disregard. Now, move the new mod into your mods folder for your instance and you're good to go!
