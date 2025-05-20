from channel_data_source import ChannelDataSource

data_source = ChannelDataSource()
nt = len(data_source)
print(f"Initialzed data source with {nt} timesteps of data")

fields = data_source.fields
print(f"Containing fields {fields}")

test_read = data_source[0]
print(f"Single snapshot has dimensions {test_read.shape}")

test_read_slice = data_source[0:10]
print(f"Read {test_read_slice.shape[0]} channel snapshots using simple slice notation")

test_read_slice = data_source[-10::2]
print(f"Read {test_read_slice.shape[0]} channel snapshots using complex slice notation")
