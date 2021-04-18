import os
import glob
import ffmpeg

in_dir = str(input("\nEnter the media drive to be ripped without any trailing \"\\\": "))
out_dir = str(input("Enter the output directory: "))
dirs_and_files = glob.glob(in_dir + "\\\\**\\\\*", recursive = True)
file_list = []
for item in dirs_and_files:
    if os.path.isfile(item):  
        file_list.append(item)        
for in_file in file_list:
    print("\nCommencing " + in_file + " ripping...")
    try:
        input = ffmpeg.input(in_file)
        in_file = in_file.replace(in_dir, "")
        out_file = out_dir + in_file
        os.makedirs(os.path.dirname(out_file), exist_ok = True)
        ffmpeg.run(ffmpeg.output(input, out_file))
        print("done!")
    except:
        print("Error: Media might not be supported")
print("\nAll operations completed!")
#Play a sound here