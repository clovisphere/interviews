package com.clovisphere.interviews.stitch

import io.restassured.RestAssured
import org.junit.jupiter.api.BeforeAll
import org.junit.jupiter.api.AfterAll
import io.restassured.specification.RequestSpecification
import io.restassured.builder.RequestSpecBuilder
import io.restassured.http.ContentType


open class BaseTest {

    companion object {
        private var requestSpecification: RequestSpecification? = null

        @BeforeAll
        @JvmStatic
        fun setup() {
            requestSpecification = RequestSpecBuilder()
                .setBaseUri("http://127.0.0.1:8080")
                .setContentType(ContentType.JSON)
                .build()
        }

        @AfterAll
        @JvmStatic
        fun teardown() {
            requestSpecification = null
            RestAssured.reset()
        }

        fun getRequestSpecification(): RequestSpecification {
            return requestSpecification!!
        }
    }
}