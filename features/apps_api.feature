Feature: Note Management API

  # 1. Создание заметок
  Scenario: Successfully create a note with valid data
    Given A valid note payload
    When I send a POST request to create a note
    Then The response status code should be 201
    And The response should contain the correct note data

  Scenario: Unsuccessfully create a note with invalid data
    Given An invalid note payload missing title
    When I send a POST request to create a note
    Then The response status code should be 422

  # 2. Получение списка заметок
  Scenario: Get note list when there are no notes
    Given The note repository is empty
    When I send a GET request to fetch all notes
    Then The response status code should be 200
    And The response list should be empty

  Scenario: Get note list when notes exist
    Given Existing notes in the system
    When I send a GET request to fetch all notes
    Then The response status code should be 200
    And The response list should not be empty

  # 3. Получение заметки по id
  Scenario: Get a single note by valid ID
    Given An existing note ID
    When I send a GET request for this note ID
    Then The response status code should be 200
    And The response should match the requested note

  Scenario: Get a single note by invalid ID
    Given An invalid note ID "99999"
    When I send a GET request for this note ID
    Then The response status code should be 404

  # 4. Редактирование заметки по id
  Scenario: Successfully update a note by valid ID
    Given An existing note ID
    And A valid note payload for update
    When I send a PUT request to update this note
    Then The response status code should be 200
    And The note should be updated successfully

  Scenario: Unsuccessfully update a note by invalid ID
    Given An invalid note ID "99999"
    And A valid note payload for update
    When I send a PUT request to update this note
    Then The response status code should be 404

  # 5. Удаление заметки по id
  Scenario: Successfully delete a note by valid ID
    Given An existing note ID
    When I send a DELETE request for this note ID
    Then The response status code should be 200

  Scenario: Unsuccessfully delete a note by invalid ID
    Given An invalid note ID "99999"
    When I send a DELETE request for this note ID
    Then The response status code should be 404
