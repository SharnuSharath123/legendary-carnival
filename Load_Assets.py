# Load images
background = pygame.image.load('background.jpg')
target_image = pygame.image.load('target.png')

# Define target position and size
target_rect = target_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
