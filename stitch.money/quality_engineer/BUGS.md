# Bugs found in the application

Let's remind ourselves of the requirements from the product team:

1. The user is able to add todo's.
2. The user is able to edit todos'.
3. The user is able to edit todos'.
4. Todo items should not be empty.
5. A todo cannot be longer than 100 characters. If it is, an error message should be thrown.
6. Once a todo is completed, it cannot be deleted.
7. The user is able to complete todos in which case they don’t get deleted and instead get a strike through.

## Frontend / UI

Below is a list of bugs I've found in the [TODO List Frontend app](https://github.com/Stitch-Money/todo-front-end):

- Strike through or completed todos can be deleted.
- Todos' name/title can exceed 100 characters.
- Todos can't be edited or modified (the functionality or feature isn't available on the Frontend).
- No error message (or hint 💭) displayed when the user tries to add an empty todo, or when the todo's name/title exceeds 100 characters.

###### Nice to have
- Disable **submit** button until the todo's name/title is entered
- Disable the **delete** and **mark as done** buttons for todos that have been completed (as per requirements)  
- Todos should be displayed in **DESCENDING** order (latest first)... Pagination, maybe? 🤔
- Add the todo's status column (visual aid).
- It'd be nice to have the todos' **id** on the page or a way of distinguishing todos since we can have "duplicate" todos.  

## Backend / API

Below is a list of bugs I've found in the [TODO List Backend API](https://github.com/Stitch-Money/todo-front-end):

- The **/todos** (POST) endpoint allows one to add todo that share or have the same **id** (or duplicate todos).
- The **/del-todos** endpoint allows one to delete todos without specifying an id - _in which case, it acts like a [stack](https://www.programiz.com/dsa/stack#:~:text=A%20stack%20is%20a%20linear,plates%20on%20top%20of%20another.)_.
- The api throw an HTTP **500** status when it can't find the todo one wants modified/edited, or when the **/edit-todos** gets no payload body.
- The **/todos** (POST) endpoint accept empty todo... No validation is done, one can send **XML** or **Plain Text** for instance.
- The api doesn't make use of the proper HTTP **verbs** and/or **status codes**. See [RESTful API's best practices](https://docs.microsoft.com/en-us/azure/architecture/best-practices/api-design#:~:text=Here%20are%20some%20of%20the,be%20accessed%20by%20the%20client.&text=REST%20APIs%20use%20a%20uniform,the%20client%20and%20service%20implementations.).
- Error messages are not returned by the api.
