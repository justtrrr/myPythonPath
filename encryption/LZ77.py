def encode_text(text):
    pack = ''
    position_i = 0
    while position_i < len(text):
        window_length = 9
        found = False
        while not found and window_length > 3:
            position_j = position_i - window_length
            while position_j >= 0 and (position_i - position_j) < 100:
                if text[position_i:position_i+window_length] == text[position_j:position_j+window_length]:
                    pack += '#%1d%2d' % (window_length, (position_i - position_j))
                    position_i += window_length
                    found = True
                    break
                position_j -= 1
            window_length -= 1
        if not found:
            pack += text[position_i]
            position_i += 1
    return pack


def decode_text(pack):
    unpack = ""
    position_i = 0
    while position_i < len(pack):
        if pack[position_i] != "#":
            unpack += pack[position_i]
            position_i += 1
            continue
        window_length = int(pack[position_i+1: position_i+2])
        dist = int(pack[position_i+2: position_i+4])
        unpack += unpack[-dist: -dist+window_length]
        position_i += 4
    return unpack


def main():
    text = 'in the back of the station wagon , church continued to pace restlessly as he had done for the last three ' \
           'days it had taken them to drive here from chicago . his yowling from the cat - kennel had been bad , ' \
           'but his restless pacing after they finally gave up and set him free in the car had been almost as ' \
           'unnerving . louis himself felt a little like crying . a wild but not unattractive idea suddenly came to ' \
           'him : he would suggest that they go back to bangor for something to eat while they waited for the moving ' \
           'van , and when his three hostages to fortune got out , he would floor the accelerator and drive away ' \
           'without so much as a look back , foot to the mat , the wagon ’ s huge four - barrel carburetor gobbling ' \
           'expensive gasoline . he would drive south , all the way to orlando , florida , where he would get a job ' \
           'at disney world as a medic , under a new name . but before he hit the turnpike – big old 95 southbound – ' \
           'he would stop by the side of the road and put the fucking cat out , too . then they rounded a final curve ' \
           'and there was the house that only he had seen up until now . he had flown out and looked at each of the ' \
           'seven possibles they had picked from photos once the position at the university was solidly his , ' \
           'and this was the one he had chosen : a big old new england colonial ( but newly sided and insulated ; the ' \
           'heating costs , while horrible enough , were not out of line in terms of consumption ) , three big rooms ' \
           'downstairs , four more up , a long shed that might be converted to more rooms later on , ' \
           'all of it surrounded by a luxuriant sprawl of lawn , lushly green even in this august heat . beyond the ' \
           'house was a large field for the children to play in , and beyond the field were woods that went on damn ' \
           'near for ever . the property abutted state lands , the realtor had explained , and there would be no ' \
           'development in the foreseeable future . the remains of the micmac indian tribe had laid claim to nearly 8 ' \
           ', 000 acres in ludlow , and in the towns east of ludlow , and the complicated litigation , involving the ' \
           'federal government as well as that of the state , might stretch into the next century . rachel stopped ' \
           'crying abruptly . she sat up . ‘ is that - ’ ‘ that ’ s it , ’ louis said . he felt apprehensive – no , ' \
           'he felt scared . in fact he felt terrified . he had mortgaged twelve years of their lives for this ; it ' \
           'wouldn ’ t be paid off until eileen was seventeen , an unbelievable age . he swallowed . ‘ what do you ' \
           'think ? ’ ‘ i think it ’ s beautiful , ’ rachel said , and that was a huge weight off his chest – and off ' \
           'his mind . she wasn ’ t kidding , he saw ; it was in the way she was looking at it as they turned in the ' \
           'asphalted driveway that swept around to the shed in back , her eyes sweeping the blank windows , ' \
           'her mind already ticking away at such matters as curtains and oilcloth for the cupboards and god knew ' \
           'what else . ‘ daddy ? ’ eileen said from the back seat . she had stopped crying as well . even gage had ' \
           'stopped fussing . louis savored the silence . ‘ what , love ? ’ her eyes , brown under darkish blonde ' \
           'hair in the rear - view mirror'
    print("text: " + text)

    pack = encode_text(text)
    print("pack: " + pack)

    unpack = decode_text(pack)
    print("unpack: " + unpack)

    print(len(pack), len(text))
    if text != unpack:
        print("Несоответствие")


if __name__ == "__main__":
    main()
