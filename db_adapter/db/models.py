import uuid
from django.db import models

class User(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    full_name = models.CharField(max_length=150)
    username = models.CharField(max_length=150, unique=True)
    account_status = models.BooleanField(default=True)
    ldap_dn = models.CharField(max_length=512)
    ldap_checked_at = models.DateTimeField()
    last_login = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"

class Role(models.Model):
    role_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role_name = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "role"

class Action(models.Model):
    action_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    action_name = models.CharField(max_length=50, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "action"

class RoleAction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "role_action"
        unique_together = ("role", "action")

class UserRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_role"
        unique_together = ("user", "role")


class UserRoleAction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    action = models.ForeignKey(Action, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_role_action"
        unique_together = ("user", "role", "action")

class ModelStatus(models.Model):
    status_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status_name = models.CharField(max_length=100, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "model_status"


class Model(models.Model):
    model_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    status = models.ForeignKey(ModelStatus, on_delete=models.PROTECT)

    model_name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    model_type = models.CharField(max_length=200)

    initiator = models.ForeignKey(User, related_name="initiated_models", on_delete=models.PROTECT)
    validator = models.ForeignKey(User, related_name="validated_models", on_delete=models.PROTECT)
    first_approver = models.ForeignKey(User, related_name="first_approved_models", on_delete=models.PROTECT)
    second_approver = models.ForeignKey(User, related_name="second_approved_models", on_delete=models.PROTECT)

    version_name = models.CharField(max_length=50)
    sop_document_path = models.TextField(null=True, blank=True)
    model_file_path = models.TextField()
    library_configuration_path = models.TextField(null=True, blank=True)
    retirement_justification = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "model"

class Document(models.Model):
    document_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)

    file_name = models.CharField(max_length=255)
    uploader = models.ForeignKey(User, on_delete=models.PROTECT)
    file_path = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "document"


class ExecutionResult(models.Model):
    result_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    executor = models.ForeignKey(User, on_delete=models.PROTECT)

    execution_status = models.TextField()
    parameters = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "results"

class Notification(models.Model):
    notification_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "notifications"


class AuditLog(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    action_name = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "logs"


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    subject = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "comments"

class PreprocessedDataset(models.Model):
    dataset_id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    dataset_name = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    sql_script_path = models.TextField()
    cached_file_path = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "preprocessed_dataset"