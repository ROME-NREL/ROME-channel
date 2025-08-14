import qoi
from channel_data_source import ChannelDataSource

data_source = ChannelDataSource()
test_snapshot = data_source[0]
z = data_source.z

qois = qoi.get_qois(test_snapshot, z)
