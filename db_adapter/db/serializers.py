from rest_framework import serializers
from .models import (
    User,
    Role,
    Action,
    RoleAction,
    UserRole,
    UserRoleAction,
    ModelStatus,
    Model,
    Document,
    ExecutionResult,
    Notification,
    AuditLog,
    Comment,
    PreprocessedDataset,
)


class UserRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "username", "full_name")


class RoleRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ("role_id", "role_name")


class ActionRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = ("action_id", "action_name")


class ModelStatusRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelStatus
        fields = ("status_id", "status_name")


class ModelRefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = ("model_id", "model_name")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("user_id", "created_at", "updated_at")


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
        read_only_fields = ("role_id", "created_at", "updated_at")


class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"
        read_only_fields = ("action_id", "created_at", "updated_at")


class RoleActionSerializer(serializers.ModelSerializer):
    role = RoleRefSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source="role", write_only=True
    )
    action = ActionRefSerializer(read_only=True)
    action_id = serializers.PrimaryKeyRelatedField(
        queryset=Action.objects.all(), source="action", write_only=True
    )

    class Meta:
        model = RoleAction
        fields = ("id", "role", "role_id", "action", "action_id", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


class UserRoleSerializer(serializers.ModelSerializer):
    user = UserRefSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )
    role = RoleRefSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source="role", write_only=True
    )

    class Meta:
        model = UserRole
        fields = ("id", "user", "user_id", "role", "role_id", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")


class UserRoleActionSerializer(serializers.ModelSerializer):
    user = UserRefSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )
    role = RoleRefSerializer(read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(
        queryset=Role.objects.all(), source="role", write_only=True
    )
    action = ActionRefSerializer(read_only=True)
    action_id = serializers.PrimaryKeyRelatedField(
        queryset=Action.objects.all(), source="action", write_only=True
    )

    class Meta:
        model = UserRoleAction
        fields = (
            "id",
            "user",
            "user_id",
            "role",
            "role_id",
            "action",
            "action_id",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "created_at", "updated_at")


class ModelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelStatus
        fields = "__all__"
        read_only_fields = ("status_id", "created_at", "updated_at")


class ModelSerializer(serializers.ModelSerializer):
    initiator = UserRefSerializer(read_only=True)
    initiator_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="initiator", write_only=True
    )

    validator = UserRefSerializer(read_only=True)
    validator_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="validator", write_only=True
    )

    first_approver = UserRefSerializer(read_only=True)
    first_approver_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="first_approver", write_only=True
    )

    second_approver = UserRefSerializer(read_only=True)
    second_approver_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="second_approver", write_only=True
    )

    status = ModelStatusRefSerializer(read_only=True)
    status_id = serializers.PrimaryKeyRelatedField(
        queryset=ModelStatus.objects.all(), source="status", write_only=True
    )

    class Meta:
        model = Model
        fields = (
            "model_id",
            "model_name",
            "description",
            "model_type",
            "status",
            "status_id",
            "initiator",
            "initiator_id",
            "validator",
            "validator_id",
            "first_approver",
            "first_approver_id",
            "second_approver",
            "second_approver_id",
            "version_name",
            "sop_document_path",
            "model_file_path",
            "library_configuration_path",
            "retirement_justification",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("model_id", "created_at", "updated_at")


class DocumentSerializer(serializers.ModelSerializer):
    model = ModelRefSerializer(read_only=True)
    model_id = serializers.PrimaryKeyRelatedField(
        queryset=Model.objects.all(), source="model", write_only=True
    )
    uploader = UserRefSerializer(read_only=True)
    uploader_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="uploader", write_only=True
    )

    class Meta:
        model = Document
        fields = (
            "document_id",
            "model",
            "model_id",
            "file_name",
            "uploader",
            "uploader_id",
            "file_path",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("document_id", "created_at", "updated_at")


class ExecutionResultSerializer(serializers.ModelSerializer):
    model = ModelRefSerializer(read_only=True)
    model_id = serializers.PrimaryKeyRelatedField(
        queryset=Model.objects.all(), source="model", write_only=True
    )
    executor = UserRefSerializer(read_only=True)
    executor_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="executor", write_only=True
    )

    class Meta:
        model = ExecutionResult
        fields = (
            "result_id",
            "model",
            "model_id",
            "executor",
            "executor_id",
            "execution_status",
            "parameters",
            "result_path",
            "logs",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("result_id", "created_at", "updated_at")


class NotificationSerializer(serializers.ModelSerializer):
    user = UserRefSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )

    class Meta:
        model = Notification
        fields = ("notification_id", "user", "user_id", "message", "is_read", "created_at", "updated_at")
        read_only_fields = ("notification_id", "created_at", "updated_at")


class AuditLogSerializer(serializers.ModelSerializer):
    user = UserRefSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )

    class Meta:
        model = AuditLog
        fields = ("log_id", "user", "user_id", "action_name", "created_at", "updated_at")
        read_only_fields = ("log_id", "created_at", "updated_at")


class CommentSerializer(serializers.ModelSerializer):
    model = ModelRefSerializer(read_only=True)
    model_id = serializers.PrimaryKeyRelatedField(
        queryset=Model.objects.all(), source="model", write_only=True
    )
    user = UserRefSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user", write_only=True
    )

    class Meta:
        model = Comment
        fields = (
            "comment_id",
            "model",
            "model_id",
            "user",
            "user_id",
            "subject",
            "content",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("comment_id", "created_at", "updated_at")


class PreprocessedDatasetSerializer(serializers.ModelSerializer):
    creator = UserRefSerializer(read_only=True)
    creator_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="creator", write_only=True
    )

    class Meta:
        model = PreprocessedDataset
        fields = (
            "dataset_id",
            "dataset_name",
            "description",
            "creator",
            "creator_id",
            "sql_script_path",
            "cached_file_path",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("dataset_id", "created_at", "updated_at")