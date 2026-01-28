#!/usr/bin/env python3
"""
Script to create a 512x512 PNG icon for Play Store
"""

try:
    from PIL import Image, ImageDraw
    import sys
    import os
except ImportError:
    print("PIL (Pillow) is required. Install it with:")
    print("  pip install Pillow")
    sys.exit(1)

def create_play_store_icon():
    """Create a 512x512 PNG icon for Play Store"""
    
    # Create a 512x512 image with WhatsApp green background
    size = 512
    img = Image.new('RGB', (size, size), color='#25D366')
    draw = ImageDraw.Draw(img)
    
    # Draw a white chat bubble in the center
    # Bubble dimensions (scaled for 512x512)
    bubble_margin = 80
    bubble_width = size - (bubble_margin * 2)
    bubble_height = bubble_width * 0.6
    bubble_x = bubble_margin
    bubble_y = (size - bubble_height) / 2
    
    # Draw rounded rectangle for chat bubble
    corner_radius = 30
    # Main bubble body
    draw.rounded_rectangle(
        [(bubble_x, bubble_y), (bubble_x + bubble_width, bubble_y + bubble_height)],
        radius=corner_radius,
        fill='#FFFFFF',
        outline=None
    )
    
    # Draw tail/pointer on the left side (pointing left)
    tail_points = [
        (bubble_x, bubble_y + bubble_height * 0.3),
        (bubble_x - 20, bubble_y + bubble_height * 0.4),
        (bubble_x, bubble_y + bubble_height * 0.5),
    ]
    draw.polygon(tail_points, fill='#FFFFFF')
    
    # Draw message lines inside the bubble
    line_y_start = bubble_y + bubble_height * 0.25
    line_spacing = 20
    line_width = bubble_width * 0.6
    line_x = bubble_x + (bubble_width - line_width) / 2
    
    # Three message lines
    for i in range(3):
        y = line_y_start + (i * line_spacing)
        line_height = 8
        if i == 2:  # Last line is shorter
            line_width = bubble_width * 0.4
            line_x = bubble_x + (bubble_width - line_width) / 2
        draw.rounded_rectangle(
            [(line_x, y), (line_x + line_width, y + line_height)],
            radius=4,
            fill='#25D366'
        )
    
    # Save the image
    output_path = 'play_store_icon_512x512.png'
    img.save(output_path, 'PNG')
    print(f"✅ Play Store icon created: {output_path}")
    print(f"   Size: {size}x{size} pixels")
    print(f"   Format: PNG")
    print(f"   Ready to upload to Play Console!")
    
    return output_path

if __name__ == '__main__':
    try:
        create_play_store_icon()
    except Exception as e:
        print(f"Error creating icon: {e}")
        sys.exit(1)
