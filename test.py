import redis



def main():
    r = redis.Redis(decode_responses=True)
    r.set('key', 'value', 10)
    print(r.get('key'))



if __name__ == "__main__":
    main()