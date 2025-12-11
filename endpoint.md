| #  | Method | Path                                          | Purpose                                                   | Owner              |
| -- | ------ | --------------------------------------------- | --------------------------------------------------------- | ------------------ |
| 1  | POST   | /auth/login                                   | Login (username/password)                                 | common             |
| 2  | GET    | /users                                        | Get all users (filter/page)                               | user-management    |
| 3  | POST   | /users                                        | Create new user (with LDAP validation)                    | user-management    |
| 4  | POST   | /users/{id}/ldap_revalidate                   | Revalidate LDAP for user                                  | user-management    |
| 5  | PATCH  | /users/{id}                                   | Edit user (partial, incl. deactivate)                     | user-management    |
| 6  | GET    | /models                                       | Get models with filters & pagination                      | model-management   |
| 7  | POST   | /models                                       | Create new model (draft)                                  | model-management   |
| 8  | PATCH  | /models/{id}                                  | Edit model metadata                                       | model-management   |
| 9  | POST   | /models/{id}/versions/request-upload          | Create document metadata + return presigned upload URL    | model-management   |
| 10 | POST   | /models/{id}/documents/{document_id}/finalize | Finalize document upload                                  | model-management   |
| 11 | POST   | /models/{id}/versions                         | Create new model version                                  | model-management   |
| 12 | GET    | /models/{id}/versions                         | Get version history                                       | model-management   |
| 13 | GET    | /models/{id}/versions/{vid}/download          | Download (presigned URL) model files                      | model-management   |
| 14 | POST   | /models/{id}/actions                          | Model lifecycle actions (validate, approve, retire, etc.) | model-management   |
| 15 | POST   | /models/{id}/comments                         | Add comment                                               | model-management   |
| 16 | GET    | /models/{id}/comments                         | Get model comments                                        | model-management   |
| 17 | POST   | /models/{id}/execute                          | Initiate model execution                                  | model-management   |
| 18 | POST   | /db/api/v1/executions                         | Create execution record (queued)                          | model-management         |
| 19 | PATCH  | /db/api/v1/executions/{result_id}             | Execution-engine callback (update status/logs/metrics)    | model-management         |
| 20 | GET    | /models/{id}/results                          | Get execution history                                     | model-management   |
| 21 | GET    | /models/{id}/results/{result_id}              | Get execution result detail                               | model-management   |
| 22 | GET    | /models/{id}/results/{result_id}/compare      | Compare execution results                                 | model-management   |
| 23 | GET    | /models/{id}/results/{result_id}/export       | Export execution result (presigned zip)                   | model-management   |
| 24 | GET    | /datasets                                     | Get all datasets                                          | dataset-management |
| 25 | POST   | /datasets                                     | Upload new SQL (presigned)                                | dataset-management |
| 26 | POST   | /datasets/{id}/trigger                        | Trigger preprocessing                                     | dataset-management |
| 27 | GET    | /datasets/{id}/download                       | Download dataset (presigned)                              | dataset-management |
| 28 | DELETE | /datasets/{id}                                | Delete dataset                                            | dataset-management |
| 29 | GET    | /notifications                                | Get notifications for logged user                         | model-management         |
| 30 | PATCH  | /notifications/{id}                           | Mark notification as read                                 | model-management         |
| 31 | GET    | /documents/{id}/download                      | Download document (presigned)                             | model-management   |
| 32 | DELETE | /documents/{id}                               | Delete document                                           | model-management   |
| 33 | GET    | /models/{id}/logs                             | Get audit logs                                            | model-management         |
