scale_pct = mymidi.linear_scaale_pct(0, 30, year)

# notes - range

d_minor = ['D', 'E', 'F', 'G']
note = mymidi.scale_to_note(scale_pct, d_minor)

# Translate note to midi pitch 

midi_pitch = mymidi.note_to_midi_pitch(note)

return midi_pitch

note_list = []
# song list 

for d in my_data:
    note_list.append([
        d['beat'] = start_time, 
        data_to_pitch_tuned(d['year']),
        100, # velocity 
        2 # duration
    ])

# Add a track

mymidi.add_track(note_list)

# output
mymidi.save_midi()
