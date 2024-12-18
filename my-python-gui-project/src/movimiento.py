def handle_keypress(event, main_window):
    row, column = main_window.current_position
    if event.keysym == 'w' and row > 0:
        row -= 1
    elif event.keysym == 's' and row < main_window.rows - 1:
        row += 1
    elif event.keysym == 'a' and column > 0:
        column -= 1
    elif event.keysym == 'd' and column < main_window.columns - 1:
        column += 1
    else:
        return

    main_window.move_image(row, column)

def move_image(main_window, new_row, new_column):
    main_window.current_image_label.pack_forget()
    main_window.add_image_to_cell(new_row, new_column)
    main_window.current_position = (new_row, new_column)