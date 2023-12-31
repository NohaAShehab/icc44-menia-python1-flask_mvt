from flask import  request, render_template, redirect, url_for
from app.tracks import track_blueprint
from app.models import  Track
from app.tracks.forms import  TrackForm


@track_blueprint.route('/create', endpoint='create', methods = ['GET', 'POST'])
def track_create():
    print(f'Request received {request}')
    if request.method=='POST':
        print(request.form)
        track = Track.save_object(requestdata=request.form)
        return  redirect(track.show_url)

    return render_template('tracks/create.html')


@track_blueprint.route('', endpoint='index')
def tracks_index():
    tracks=  Track.get_all_tracks()
    return render_template('tracks/index.html', tracks=tracks)

@track_blueprint.route('/<int:id>', endpoint='show')
def track_show(id):
    track=  Track.get_specific_track(id)
    return render_template('tracks/show.html', track=track)

@track_blueprint.route('/<int:id>/delete', endpoint='delete')
def track_delete(id):
    Track.delete_object(id)
    # redirect
    return  redirect(url_for('tracks.index'))


@track_blueprint.route('/create/forms', endpoint='formcreate', methods = ['GET', 'POST'])
def track_form_create():
    form = TrackForm()
    if request.method=='POST':
        if form.validate_on_submit():

        ## remove csrf_token ? from send data
            print(request.form)
            request_data = dict(request.form)
            del request_data['csrf_token']
            track = Track.save_object(requestdata=request_data)
            return  redirect(track.show_url)

    return render_template('tracks/createform.html', form=form)