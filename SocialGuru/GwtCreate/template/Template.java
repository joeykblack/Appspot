/**
 * 
 */
package project.gwt.package.client;

import project.gwt.package.client.factory.ClientFactory;
import project.gwt.package.client.factory.impl.ClientFactoryImpl;
import project.gwt.package.client.mvp.AppActivityMapper;
import project.gwt.package.client.mvp.AppPlaceHistoryMapper;
import project.gwt.package.client.place.TemplatePlace;
import project.gwt.package.client.gin.TemplateGinjector;

import com.google.gwt.activity.shared.ActivityManager;
import com.google.gwt.activity.shared.ActivityMapper;
import com.google.gwt.core.client.EntryPoint;
import com.google.gwt.core.client.GWT;
import com.google.gwt.place.shared.Place;
import com.google.gwt.place.shared.PlaceHistoryHandler;
import com.google.gwt.user.client.ui.RootPanel;
import com.google.gwt.user.client.ui.SimplePanel;

/**
 * @author joey
 *
 */
public class Template implements EntryPoint 
{
	public static final TemplateGinjector injector = GWT.create(TemplateGinjector.class);
	public static final ClientFactory factory = new ClientFactoryImpl();
	private Place defaultPlace = new TemplatePlace("Template");
	private SimplePanel appWidget = new SimplePanel();

	/* (non-Javadoc)
	 * @see com.google.gwt.core.client.EntryPoint#onModuleLoad()
	 */
	@Override
	public void onModuleLoad() 
	{
		// Start ActivityManager for the main widget with our ActivityMapper
		ActivityMapper activityMapper = new AppActivityMapper();
		ActivityManager activityManager = new ActivityManager(activityMapper, factory.getEventbus());
		activityManager.setDisplay(appWidget);

		// Start PlaceHistoryHandler with our PlaceHistoryMapper
		AppPlaceHistoryMapper historyMapper= GWT.create(AppPlaceHistoryMapper.class);
		PlaceHistoryHandler historyHandler = new PlaceHistoryHandler(historyMapper);
		historyHandler.register(factory.getPlacecontroller(), factory.getEventbus(), defaultPlace);

		RootPanel.get().add(appWidget);
		// Goes to place represented on URL or default place
		historyHandler.handleCurrentHistory();
	}

}
