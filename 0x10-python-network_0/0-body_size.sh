# check if URL is provided
if [ -z "$1" ]; then
  echo "Usage: $0 URL"
  exit 1
fi

# send request to URL and save response to a temporary file
curl -s "$1" -o /tmp/response.txt

# get size of response body in bytes
size=$(wc -c < /tmp/response.txt)

# display size of response body
echo $size

# remove temporary file
rm /tmp/response.txt
