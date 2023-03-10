Feature: Identity OCR API

  Scenario: Identity OCR with valid image
    Given input a image with "/path/valid_image.jpg"
    When calling OCR API with image
    Then verify the response status is successfully
    Then verify the response fields contain ID, Name, Birthday and Address

  Scenario: Identity OCR with invalid image
    Given input a image with "/path/invalid_image.jpg"
    When calling OCR API with image
    Then verify the response status is failure

  Scenario: Identity OCR with no image
    Given input a image with "no_image"
    When calling OCR API with image
    Then verify the response status code is 400
    Then verify the response contain error field


