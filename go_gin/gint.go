package main

import "github.com/gin-gonic/gin"

func main() {
	r := gin.New()
	r.GET("/json", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "Hello, world!",
		})
	})
	r.Run(":5000")
}
