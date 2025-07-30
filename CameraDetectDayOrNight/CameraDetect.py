import sys

def ImageDayNightMode() -> str:
    """
    Args:
    None
    Returns: str with day/night prediction image based in 2D Grid pixel values in stdin format
    lum variable is defined follows ITU-R BT.601 technical standard for analog TV and digital video. Green -> best perception by human vision, red -> intermediate, blue -> worst perception by human vision. The code successfully passed all 16 unit tests on the HackerRank platform.
    """
    
    total_intensity = 0
    num_pixels = 0
    
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        pixels = line.split()
        for pixel in pixels:
            b, g, r = map(int, pixel.split(','))
            # Follows ITU-R BT.601 technical standard for analog TV and digital video. Green -> best perception by human vision, red -> intermediate, blue -> worst perception by human vision
            lum = 0.299*r + 0.114*b + 0.587*g 
            total_intensity += lum
            num_pixels += 1
    
    avg_intensity = total_intensity / num_pixels
    
    if avg_intensity >= 100:
        print('day')
    else:
        print('night')
        

if __name__=='__main__':
    ImageDayNightMode()
        
        
    
