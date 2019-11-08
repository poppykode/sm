from rest_framework import serializers

from enquiries.models import Enquiry

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields =('title','company','contact_name','email','phone_number','priority','assigned_to','channel','service','value','status','next_follow_up','attended_to','next_follow_up_time','decription','website','service_mode','address')

class SalesFunnelSerialize(serializers.Serializer):
    new = serializers.CharField(required=False, allow_blank=True, max_length=100)
    open = serializers.CharField(required=False, allow_blank=True, max_length=100)
    won = serializers.CharField(required=False, allow_blank=True, max_length=100)
