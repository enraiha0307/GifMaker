import imageio
import os

clip = os.path.abspath('./videos/coffee_pouring.mp4')

print(clip)

#Defining the function to convert video to gif

def gifMaker(inputPath, targetFormat):

    #This wil return like array of words[coffee,.mp4] then + the targetFormat so coffee.gif
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

    print(f'converting{inputPath} \n to {outputPath}')

    reader = imageio.get_reader(inputPath) #getting imageio to read our video file
    fps = reader.get_meta_data()['fps'] #storing the original video's fps in var fps

    writer = imageio.get_writer(outputPath, fps=fps)
    #use above fps for our gif 

    for frames in reader:       #reading each frame in our video
        writer.append_data(frames)
        print(f'Frames{frames}')

    print('Done!')
    writer.close()

gifMaker(clip,'.gif')