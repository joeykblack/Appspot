package project.gwt.package.client.mvp;

import com.google.gwt.activity.shared.AbstractActivity;
import com.google.gwt.activity.shared.Activity;
import com.google.gwt.activity.shared.ActivityMapper;
import com.google.gwt.place.shared.Place;

import project.gwt.package.client.place.TemplatePlace;
import project.gwt.package.client.Template;

public class AppActivityMapper implements ActivityMapper 
{

	public AppActivityMapper() 
	{
		super();
	}

	/**
	 * Map each Place to its corresponding Activity.
	 */
	@Override
	public Activity getActivity(Place place) 
	{
		AbstractActivity activity = null;
		
		if (place instanceof TemplatePlace)
		{
			activity = Template.injector.getTemplateActivityImpl();
		}

		return activity;
	}

}
