package com.clovisphere.interviews.stitch

import com.beust.klaxon.Klaxon
import io.restassured.module.kotlin.extensions.Given
import io.restassured.module.kotlin.extensions.When
import io.restassured.module.kotlin.extensions.Then
import org.apache.http.HttpStatus
import org.hamcrest.CoreMatchers.*
import org.hamcrest.Matchers.anyOf
import org.hamcrest.Matchers.`is`
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.TestMethodOrder
import org.junit.jupiter.api.MethodOrderer.OrderAnnotation
import org.junit.jupiter.api.Order
import kotlin.test.Ignore

// we can do better, I think 😣
// TODO: refactor
const val ID_OF_THE_NEWLY_CREATED_TODO = 3

@TestMethodOrder(OrderAnnotation::class)
class APITest: BaseTest() {

    @Test
    @Order(1)
    fun `Fetch all todos`() {
        Given {
            spec(getRequestSpecification())
        } When {
            get("/todos")
        } Then {
            statusCode(HttpStatus.SC_OK)
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // this assumes that the app has two (default) todos on startup
            body("size()", equalTo(2))
        }
    }

    @Test
    @Order(7)
    fun `Add new todo without specifying an id`(){
        val todo: Map<String, Any> = mapOf(
            "status" to "in progress",
            "todo" to "Learn Rust"
        )

        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            post("/todos")
        } Then {
            // the return status code should be a 201... 200 is okay too, but 201 is the right one
            statusCode(anyOf(`is`(HttpStatus.SC_OK), `is`(HttpStatus.SC_CREATED)))
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world, the api would return the id of the newly created item
            //body("id", equalTo(4))
            // NOTE: since the api returns all todos, the newly created item should be in the list of todos
            body("todos.find { it.id == 4 }.todo", equalTo("Learn Rust"))
        }
    }

    @Test
    @Order(2)
    fun `Add new todo by specifying an id`() {
        val todo: Map<String, Any> = mapOf(
            "id" to ID_OF_THE_NEWLY_CREATED_TODO,
            "status" to "in progress",
            "todo" to "Learn Kotlin"
        )

        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            post("/todos")
        } Then {
            // the return status code should be a 201... 200 is okay too, but 201 is the right one
            statusCode(anyOf(`is`(HttpStatus.SC_OK), `is`(HttpStatus.SC_CREATED)))
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world, the api would return the id of the newly created item
            //body("id", equalTo(ID_OF_THE_NEWLY_CREATED_TODO))
            // NOTE: since the api returns all todos, we can check if the newly created one is there
            body("find { it.id == $ID_OF_THE_NEWLY_CREATED_TODO }.id", equalTo(ID_OF_THE_NEWLY_CREATED_TODO))
        }
    }

    /**
     * This test is not working,
     * because the API doesn't support fetching a single todo.
     * We will ignore it for now.
     */
    @Test
    @Order(3)
    @Ignore
    fun `Fetch todo by id`() {
        Given {
            spec(getRequestSpecification())
        } When {
            get("/todos/$ID_OF_THE_NEWLY_CREATED_TODO")
        } Then {
            // the return status code should be a 200
            statusCode(HttpStatus.SC_OK)
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // we'd get the id of the deleted item
            body("id", equalTo(ID_OF_THE_NEWLY_CREATED_TODO))
        }
    }

    @Test
    @Order(3)
    fun `Edit or modify todo by id`() {
        val todo: Map<String, Any> = mapOf("id" to ID_OF_THE_NEWLY_CREATED_TODO, "status" to "done")

        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            post("/edit-todos")
        } Then {
            // the return status code should be a 200 or 204
            statusCode(anyOf(`is`(HttpStatus.SC_OK), `is`(HttpStatus.SC_NO_CONTENT)))
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world, the api would return the id of the updated item
            //body("id", equalTo(ID_OF_THE_NEWLY_CREATED_TODO))
            // NOTE: since the api returns all todos, we can check that modified item is there and has the right status
            body("find { it.id == $ID_OF_THE_NEWLY_CREATED_TODO }.status", equalTo("done"))
        }
    }

    @Test
    @Order(3)
    fun `Delete todo by id`() {
        val todo: Map<String, Any> = mapOf("id" to ID_OF_THE_NEWLY_CREATED_TODO)
        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            post("/del-todos")
        } Then {
            // the return status code should be a 200 or 204
            statusCode(anyOf(`is`(HttpStatus.SC_OK), `is`(HttpStatus.SC_NO_CONTENT)))
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world, the api would return the id of the deleted item
            //body("id", equalTo(ID_OF_THE_NEWLY_CREATED_TODO))
            // NOTE: the api returns all todos, we can verify that the deleted one is not there
            body("find { it.id == $ID_OF_THE_NEWLY_CREATED_TODO }.id", equalTo(null))
        }
    }

    @Test
    @Order(4)
    fun `Edit or modify todo by id using the right HTTP verb (PUT)`() {
        val todo: Map<String, Any> = mapOf("id" to ID_OF_THE_NEWLY_CREATED_TODO, "status" to "to be modified")

        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            put("/edit-todos")
        } Then {
            // the return status code should be a 200 or 204
            statusCode(anyOf(`is`(HttpStatus.SC_OK), `is`(HttpStatus.SC_NO_CONTENT)))
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world, the api would return the id of the updated item
            //body("id", equalTo(ID_OF_THE_NEWLY_CREATED_TODO))
            // NOTE: since the api returns all todos, we can check that modified item is there and has the right status
            body("find { it.id == $ID_OF_THE_NEWLY_CREATED_TODO }.status", equalTo("to be modified"))
        }
    }

    @Test
    @Order(4)
    fun `Delete todo by id using the right HTTP verb (DELETE)`() {
        val todo: Map<String, Any> = mapOf("id" to ID_OF_THE_NEWLY_CREATED_TODO)
        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            delete("/del-todos")
        } Then {
            // the return status code should be a 200 or 204
            statusCode(anyOf(`is`(HttpStatus.SC_OK), `is`(HttpStatus.SC_NO_CONTENT)))
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world, the api would return the id of the deleted item
            //body("id", equalTo(ID_OF_THE_NEWLY_CREATED_TODO))
            // NOTE: the api returns all todos, we can verify that the deleted one is not there
            body("find { it.id == $ID_OF_THE_NEWLY_CREATED_TODO }.id", equalTo(null))
        }
    }

    @Test
    @Order(5)
    fun `One shouldn't be allowed to create an empty todo`() {
        Given {
            spec(getRequestSpecification())
        } When {
            post("/todos")
        } Then {
            // the return status code should be a 400
            statusCode(HttpStatus.SC_BAD_REQUEST)
            // in a perfect world the api would return a proper error message,
            // something along the lines of "key 'id' is required"
            body("error", containsString("required"))
        }
    }

    @Test
    @Order(5)
    fun `One shouldn't be allowed to edit a todo without specifying an id`() {
        Given {
            spec(getRequestSpecification())
        } When {
            put("/edit-todos")
        } Then {
            // the return status code should be a 400
            statusCode(HttpStatus.SC_BAD_REQUEST)
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world the api would return a proper error message,
            // something along the lines of "key 'id' is required"
            body("error", containsString("required"))
        }
    }

    @Test
    @Order(5)
    fun `One shouldn't be allowed to delete a todo without specifying an id`() {
        Given {
            spec(getRequestSpecification())
        } When {
            put("/del-todos")
        } Then {
            // the return status code should be a 400
            statusCode(HttpStatus.SC_BAD_REQUEST)
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world the api would return a proper error message,
            // something along the lines of "key 'id' is required"
            body("error", containsString("required"))
        }
    }

    @Test
    @Order(2)
    fun `One shouldn't be allowed to create a todo using an existing id`() {
        val todo: Map<String, Any> = mapOf(
            "id" to 1,
            "status" to "in progress",
            "todo" to "Learn Rust"
        )

        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            post("/todos")
        } Then {
            // the return status code should be a 400
            statusCode(HttpStatus.SC_BAD_REQUEST)
        }
    }

    @Test
    @Order(6)
    fun `A todo cannot be longer than 100 characters`() {
        val text = """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
            sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
            Non diam phasellus vestibulum lorem sed. Sit amet consectetur adipiscing elit duis. 
            Phasellus vestibulum lorem sed risus ultricies tristique nulla aliquet enim. 
            Et malesuada fames ac turpis egestas maecenas. Vitae justo eget magna fermentum iaculis eu non. 
            Diam quam nulla porttitor massa id neque. Nec ullamcorper sit amet risus nullam eget. 
            Quam lacus suspendisse faucibus interdum posuere lorem ipsum dolor. Lacus sed viverra tellus in. 
            Blandit volutpat maecenas volutpat blandit. At lectus urna duis convallis convallis.
        """.trimIndent()

        val todo: Map<String, String> = mapOf("status" to "in progress", "todo" to text)

        Given {
            spec(getRequestSpecification())
            body(Klaxon().toJsonString(todo))
        } When {
            post("/todos")
        } Then {
            // the return status code should be a 400
            statusCode(HttpStatus.SC_BAD_REQUEST)
            // MIME media type for JSON text is application/json
            // see RFC 4627 ~ https://www.ietf.org/rfc/rfc4627.txt
            //header("Content-Type", equalTo("application/json"))
            // in a perfect world, the api will return an error message
            body("error", equalTo("Todo cannot be longer than 100 characters"))
        }
    }

}
