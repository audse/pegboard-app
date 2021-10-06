export type UserSimple = {
    id:number,
    username:string,
}

export type Color = {
    id:number,
    user:UserSimple,

    board:number,
    
    name:string,
    code:string,
}

export type Tag = {
    id:number,
    user:UserSimple,

    board:number,

    color:number,
    name:string,
}

export type ChecklistItem = {
    done:boolean,
    name:string|null,
}

export type ChecklistForm = {
    board?:number,
    page?:number,
    note?:number,

    name:string,
    items:Array<ChecklistItem>
}

export type Checklist = {
    id:number,
    user:UserSimple,

    board:number|null,
    page:number|null,
    note:number|null,

    name:string|null,
    items:Array<ChecklistItem>,
}

export type UserComment = {
    id:number,
    user:UserSimple,

    board:number|null,
    page:number|null,
    note:number|null,

    content:string,

    date_created:string,
    date_edited:string,
    date_archived:string|null,
}

export type Note = {
    id:number,
    user:UserSimple,

    page:number|null,
    board:number|null,

    name:string, 
    content:string|null,

    display:string,
    url:string,
    order:number,

    starred:boolean,
    pinned:boolean,
    marked_done:boolean,

    tags:Array<Tag>, 

    assigned_to:UserSimple|null,
    date_due:string|null,
    date_todo:string|null,
    date_created:string,
    date_updated:string,
    date_archived:string|null,

    comments:Array<UserComment>
    checklists:Array<Checklist>
}

export type Page = {
    id:number,
    user:UserSimple,

    board:number,

    name:string,
    description:string|null,

    notes:Array<Note>,

    url:string,
    order:number,
    
    tags:Array<Tag>,

    assigned_to:UserSimple|null,
    date_created:string,
    date_updated:string,
    date_archived:string|null,

    comments:Array<UserComment>
    checklists:Array<Checklist>,
}

export type Board = {
    id:number,
    user:UserSimple,
    shared_with:Array<UserSimple>,

    folder:number|null,

    name:string,
    description:string|null,

    pages:Array<Page>,
    notes:Array<Note>,

    url:string,
    order:number,

    default_note_display:string,

    date_created:string,
    date_updated:string,
    date_archived:string|null,

    comments:Array<UserComment>,
    checklists:Array<Checklist>,
    colors:Array<Color>,
}

export type Folder = {
    id:number,
    user:UserSimple,

    name:string,
    description:string|null,

    boards:Array<Board>,

    url:string,
    order:number,

    date_created:string,
    date_updated:string,
    date_archived:string|null,
}