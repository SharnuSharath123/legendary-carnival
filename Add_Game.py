def main():
    running = True
    score = 0
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            # Handle mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if target_rect.collidepoint(mouse_x, mouse_y):
                    score += 1
                    print(f'Score: {score}')
        
        # Clear the screen
        screen.fill(WHITE)
        
        # Draw background and target
        screen.blit(background, (0, 0))
        screen.blit(target_image, target_rect.topleft)
        
        # Update the display
        pygame.display.flip()
        
        # Frame rate
        clock.tick(60)
