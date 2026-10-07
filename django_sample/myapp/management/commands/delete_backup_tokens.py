from django.core.management.base import BaseCommand
from django_otp.plugins.otp_static.models import StaticDevice, StaticToken


class Command(BaseCommand):
    help = "発行済みのユーザーバックアップトークン（StaticDevice/StaticToken）を全削除します"

    def add_arguments(self, parser):
        # 実行時の確認用フラグ (--force オプション)
        parser.add_argument(
            "--force",
            action="store_true",
            help="確認プロンプトをスキップして即時削除します",
        )

    def handle(self, *args, **options):
        # 削除対象の件数を取得
        device_count = StaticDevice.objects.filter(user__is_staff=False).count()
        token_count = StaticToken.objects.filter(device__user__is_staff=False).count()

        if device_count == 0 and token_count == 0:
            self.stdout.write(
                self.style.SUCCESS(
                    "削除対象のユーザーバックアップトークンはありませんでした。"
                )
            )
            return

        self.stdout.write(f"削除対象: Device {device_count}件, Token {token_count}件")

        # --force オプションがない場合は確認を挟む
        if not options["force"]:
            confirm = input(
                "本当にすべてのユーザーバックアップトークンを削除しますか？ (y/N): "
            )
            if confirm.lower() != "y":
                self.stdout.write(self.style.WARNING("処理を中断しました。"))
                return

        # 削除処理を実行（StaticDevice を削除すると関連する StaticToken も CASCADE 削除されます）
        deleted_devices, _ = StaticDevice.objects.filter(user__is_staff=False).delete()

        self.stdout.write(
            self.style.SUCCESS(
                f"正常に削除が完了しました。（削除件数: {deleted_devices}件）"
            )
        )
