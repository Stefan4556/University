import Model.MessageTask;
import Model.Task;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Predicate;
import java.util.stream.Collectors;

public class RunFilters {

    public static <E> List<E> filterTask(List<E> list, Predicate<E> predicate){

        List<E> result = list.stream().filter(predicate).collect(Collectors.toList());

        return result;
    }

    public static List<Task> filterTaskByDescription(List<Task> list, String word){

        Predicate<Task> taskPredicate = task -> task.getDescription().contains(word);

        return filterTask(list, taskPredicate);
    }

    public static void main(String[] args){

        List<Task> taskList = new ArrayList<>();

        taskList.add(new MessageTask("1","Descriere1", "Mesaj1", "Ana","Bibi", LocalDateTime.now()));
        taskList.add(new MessageTask("2","sportActivity", "Mesaj2", "Diana","Alex", LocalDateTime.now()));
        taskList.add(new MessageTask("3","readingActivity", "Mesaj3", "Alex","Andrei", LocalDateTime.now()));

        filterTaskByDescription(taskList, "sport").forEach(System.out::println);
    }
}
