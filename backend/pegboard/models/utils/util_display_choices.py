
DISPLAY_CHOICES = [
    ('n', 'note'), # default view: notecard with truncated text
    ('h', 'heading'), # bigger/bolder text
    ('i', 'image'), # shows only image
    ('c', 'checkbox'), # big checkbox on front of note for easy mark done
    ('a', 'assignee'), # emphasizes the assignee with their avatar on the front
    ('r', 'readme'), # longer text field with markdown
    ('s', 'small'), # a smaller/denser `note` view
    ('l', 'checklist'), # displays checklist prominently, good for headings
    ('d', 'date'), # displays due date/todo date prominently, with colors to indicate soonness
    ('o', 'countdown'), # displays due date/todo date prominently, with a countdown to indicate soonness
    ('t', 'discussion') # displays comments/live chat on front 
]